#!/usr/bin/env python3
"""Run mdformat on all .md files to auto-format them.

Prints each file as it is formatted.
"""

import subprocess
import sys
from pathlib import Path


def find_markdown_files(root: Path) -> list[Path]:
    """Recursively find all .md files under root."""
    return sorted(root.rglob("*.md"))


def format_file(filepath: Path) -> bool:
    """Run mdformat on a single file. Returns True on success."""
    result = subprocess.run(
        ["mdformat", str(filepath)],
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

    errors = 0

    for filepath in md_files:
        relative = filepath.relative_to(repo_root)
        if format_file(filepath):
            print(f"  Formatted  {relative}")
        else:
            print(f"  Error      {relative}")
            errors += 1

    print(f"\nFormatting complete: {len(md_files) - errors} formatted, {errors} errors.")

    return 1 if errors > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
