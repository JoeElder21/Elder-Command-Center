#!/usr/bin/env python3
"""Run lint + validate_templates + check_naming in sequence.

Prints a summary with pass/fail counts and exits 1 if any check fails.
"""

import subprocess
import sys
from pathlib import Path

CHECKS = [
    ("Lint (mdformat --check)", "lint.py"),
    ("Validate Templates", "validate_templates.py"),
    ("Check Naming", "check_naming.py"),
]


def run_check(tools_dir: Path, script_name: str) -> bool:
    """Run a single check script. Returns True if it passes (exit code 0)."""
    script_path = tools_dir / script_name
    result = subprocess.run(
        [sys.executable, str(script_path)],
        cwd=tools_dir.parent,
    )
    return result.returncode == 0


def main() -> int:
    tools_dir = Path(__file__).resolve().parent
    passed = 0
    failed = 0
    results: list[tuple[str, bool]] = []

    for label, script in CHECKS:
        print(f"\n{'=' * 60}")
        print(f"Running: {label}")
        print("=" * 60)

        success = run_check(tools_dir, script)
        results.append((label, success))

        if success:
            passed += 1
        else:
            failed += 1

    # Print summary.
    print(f"\n{'=' * 60}")
    print("TEST SUMMARY")
    print("=" * 60)

    for label, success in results:
        status = "PASS" if success else "FAIL"
        print(f"  [{status}]  {label}")

    print(f"\nTotal: {passed} passed, {failed} failed out of {len(results)} checks.")

    return 1 if failed > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
