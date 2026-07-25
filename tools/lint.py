#!/usr/bin/env python3
"""Run mdformat --check on all .md files recursively.

Prints pass/fail for each file and exits 1 if any file fails the format check.
"""

import subprocess
import sys
from pathlib import Path


def find_markdown_files(root: Path) -> list[Path]:
    """Recursively find all .md files under root."""
    return sorted(root.rglob("*.md"))


def check_file(filepath: Path) -> bool:
    """Run mdformat --check on a single file. Returns True if the file passes."""
    result = subprocess.run(
        ["mdformat", "--check", str(filepath)],
        capture_output=True,
        text=True,
    )
    return result.returncode == 0


def main() -> int:
    repo_root = Path(__file__).resolve().parent.parent
    md_files = find_markdown_files(repo_root)

    if not md_files:
        print("No .md files found.")
        return 0

    passed = 0
    failed = 0

    for filepath in md_files:
        relative = filepath.relative_to(repo_root)
        if check_file(filepath):
            print(f"  PASS  {relative}")
            passed += 1
        else:
            print(f"  FAIL  {relative}")
            failed += 1

    print(f"\nLint summary: {passed} passed, {failed} failed out of {passed + failed} files.")

    return 1 if failed > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
