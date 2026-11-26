#!/usr/bin/env python3
"""Lean plugin profile: load only the plugins you really use, keep every other plugin one command away.

    python tools/claude_profile.py plan    [--top 15] [--days 90]
    python tools/claude_profile.py lean    [--top 15] [--days 90] [--apply]
    python tools/claude_profile.py full    [--apply]
    python tools/claude_profile.py enable  NAME [--apply]
    python tools/claude_profile.py disable NAME [--apply]

Dry run unless --apply. Uses only the documented `claude plugin enable|disable|list` commands, so no settings
file is edited by hand. `lean` saves the pre-lean plugin list so `full` can restore it. Plugin hooks stop when
their plugin is disabled, so a lean profile also cuts hooks; `plan` shows how many hook groups it keeps.
"""

import argparse
import json
import shutil
import subprocess
import sys
import time

from plugin_usage import CLAUDE_DIR, count_hooks, count_usage

STATE = CLAUDE_DIR / "plugin-profile.json"


def claude(args: list[str], apply: bool) -> str:
    """Run `claude <args>` (or just print it on a dry run). Returns stdout."""
    print("  $ claude " + " ".join(args) + ("" if apply else "   (dry run)"))
    if not apply:
        return ""
    exe = shutil.which("claude") or sys.exit("claude CLI not found on PATH")
    done = subprocess.run([exe, *args], capture_output=True, text=True, check=False)
    if done.returncode != 0:
        print("    failed:", (done.stderr or done.stdout).strip()[:200])
    return done.stdout


def plugin_list() -> list[dict]:
    """Installed plugins from `claude plugin list --json` (a list of {id, enabled, ...})."""
    exe = shutil.which("claude")
    if exe is None:
        return []
    out = subprocess.run([exe, "plugin", "list", "--json"], capture_output=True, text=True, check=False).stdout
    try:
        data = json.loads(out)
    except json.JSONDecodeError:
        return []
    items = data if isinstance(data, list) else data.get("plugins", [])
    return [item for item in items if isinstance(item, dict) and item.get("id")]


def enabled_plugins() -> list[str]:
    """Ids of the plugins that are enabled right now."""
    return [item["id"] for item in plugin_list() if item.get("enabled", True)]


def name_to_id() -> dict[str, str]:
    """Map a bare plugin name to its installed id. The CLI rejects bare names with an ambiguous-marketplace error."""
    return {item["id"].split("@")[0]: item["id"] for item in plugin_list()}


def resolve(name: str, ids: dict[str, str]) -> str:
    """Return the `name@marketplace` id for `name` when it is installed, else `name` unchanged."""
    return name if "@" in name else ids.get(name, name)


def plan(top: int, days: int) -> list[str]:
    """Print the usage ranking and the keep list; return the plugin names to keep."""
    uses, hooks = count_usage(CLAUDE_DIR / "projects", days), count_hooks(CLAUDE_DIR / "plugins")
    keep = [name for name, _ in uses.most_common(top)]
    print(f"Top {top} plugins by use in the last {days} days:")
    for rank, name in enumerate(keep, start=1):
        print(f"  {rank:>2}. {name:<28} uses={uses[name]:<5} hook groups={hooks.get(name, 0)}")
    kept = sum(hooks.get(name, 0) for name in keep)
    print(f"\nHook groups the lean set keeps: {kept} (goal: 3 or fewer)")
    if kept > 3:
        heavy = sorted(keep, key=lambda n: -hooks.get(n, 0))[:5]
        print("  Largest hook sources in the keep list: " + ", ".join(f"{n}={hooks.get(n, 0)}" for n in heavy))
        print("  Swap one out, or start a lean session with hooks off: claude --settings '{\"disableAllHooks\": true}'")
    return keep


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("command", choices=["plan", "lean", "full", "enable", "disable"])
    parser.add_argument("name", nargs="?")
    parser.add_argument("--top", type=int, default=15)
    parser.add_argument("--days", type=int, default=90)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    if args.command == "plan":
        plan(args.top, args.days)
    elif args.command == "lean":
        keep = plan(args.top, args.days)
        if not keep:
            return print("\nNo usage found, so nothing to keep. Not touching your plugins.") or 1
        if args.apply:
            STATE.write_text(json.dumps({"saved": time.strftime("%Y-%m-%d %H:%M"), "enabled_before": enabled_plugins()}))
        ids = name_to_id()
        for name in keep:
            if ids and name not in ids:
                print(f"  note: {name} is not installed here, skipping it")
        print("\nLean profile:")
        claude(["plugin", "disable", "--all"], args.apply)
        for name in keep:
            if not ids or name in ids:
                claude(["plugin", "enable", resolve(name, ids)], args.apply)
        print("\nRestore everything later: python tools/claude_profile.py full --apply")
    elif args.command == "full":
        before = json.loads(STATE.read_text())["enabled_before"] if STATE.exists() else []
        if not before:
            return print("No saved pre-lean list; enable plugins one at a time with `enable NAME`.") or 1
        for plugin in before:
            claude(["plugin", "enable", plugin], args.apply)
    else:
        if not args.name:
            parser.error(f"{args.command} needs a plugin NAME")
        claude(["plugin", args.command, resolve(args.name, name_to_id())], args.apply)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
