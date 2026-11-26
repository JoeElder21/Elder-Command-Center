#!/usr/bin/env python3
"""Rank Claude Code plugins by actual use, and show how many hooks each one adds.

Run on the machine whose sessions you want measured (it reads local transcripts):

    python tools/plugin_usage.py [--days 90] [--top 15]

Counts, per plugin: Skill calls ("plugin:skill"), subagent calls ("plugin:agent") and
MCP tool calls ("mcp__plugin_<plugin>_<server>__tool"). Read-only: it changes nothing.
"""

import argparse
import json
import time
from collections import Counter
from pathlib import Path

CLAUDE_DIR = Path.home() / ".claude"


def plugin_from_mcp(tool_name: str) -> str | None:
    """Return the plugin name from an `mcp__plugin_<plugin>_<server>__tool` name."""
    parts = tool_name.split("__")
    if len(parts) < 3 or not parts[1].startswith("plugin_"):
        return None
    return parts[1][len("plugin_"):].rsplit("_", 1)[0]


def count_usage(projects_dir: Path, days: int) -> Counter[str]:
    """Count plugin uses across transcripts modified in the last `days` days."""
    cutoff = time.time() - days * 86400
    uses: Counter[str] = Counter()
    for transcript in projects_dir.rglob("*.jsonl"):
        if transcript.stat().st_mtime < cutoff:
            continue
        for line in transcript.read_text(errors="ignore").splitlines():
            try:
                content = json.loads(line).get("message", {}).get("content", [])
            except (json.JSONDecodeError, AttributeError):
                continue
            for block in content if isinstance(content, list) else []:
                if not isinstance(block, dict) or block.get("type") != "tool_use":
                    continue
                name, args = block.get("name", ""), block.get("input", {}) or {}
                label = args.get("skill") if name == "Skill" else args.get("subagent_type") if name in ("Agent", "Task") else None
                if isinstance(label, str) and ":" in label:
                    uses[label.split(":", 1)[0]] += 1
                elif (plugin := plugin_from_mcp(name)) is not None:
                    uses[plugin] += 1
    return uses


def count_hooks(plugins_dir: Path) -> Counter[str]:
    """Count hook groups per plugin from each plugin's hooks.json."""
    hooks: Counter[str] = Counter()
    for hooks_file in plugins_dir.rglob("hooks.json"):
        manifest = hooks_file.parent.parent / ".claude-plugin" / "plugin.json"
        try:
            name = json.loads(manifest.read_text())["name"]
            hooks[name] += sum(len(v) for v in json.loads(hooks_file.read_text()).get("hooks", {}).values())
        except (OSError, KeyError, json.JSONDecodeError):
            continue
    return hooks


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--days", type=int, default=90)
    parser.add_argument("--top", type=int, default=15)
    args = parser.parse_args()

    uses = count_usage(CLAUDE_DIR / "projects", args.days)
    hooks = count_hooks(CLAUDE_DIR / "plugins")
    print(f"Plugin use in the last {args.days} days (transcripts: {CLAUDE_DIR / 'projects'})\n")
    print("| Rank | Plugin | Uses | Hook groups |\n|------|--------|------|-------------|")
    for rank, (plugin, n) in enumerate(uses.most_common(args.top), start=1):
        print(f"| {rank} | {plugin} | {n} | {hooks.get(plugin, 0)} |")
    keep = {plugin for plugin, _ in uses.most_common(args.top)}
    noisy = sorted(((n, p) for p, n in hooks.items() if p not in keep), reverse=True)
    print(f"\nHook groups from plugins outside the top {args.top}: {sum(n for n, _ in noisy)} (largest first)")
    for n, plugin in noisy[:10]:
        print(f"- {plugin}: {n}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
