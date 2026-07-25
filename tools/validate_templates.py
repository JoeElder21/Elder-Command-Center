#!/usr/bin/env python3
"""Validate template files in the templates/ directory.

Checks each template for:
  - H1 heading present
  - Pipe tables present
  - "Assumptions" section present
  - "Risk Flags" section present

Prints pass/fail per template and exits 1 if any template fails validation.
"""

import re
import sys
from pathlib import Path

REQUIRED_CHECKS: list[tuple[str, str, re.Pattern[str]]] = [
    ("H1 heading", "Missing H1 heading (# ...)", re.compile(r"^# .+", re.MULTILINE)),
    ("Pipe table", "No pipe table found", re.compile(r"^\|.+\|", re.MULTILINE)),
    ("Assumptions section", 'Missing "Assumptions" section', re.compile(r"^#{1,6}\s+.*Assumptions", re.MULTILINE)),
    ("Risk Flags section", 'Missing "Risk Flags" section', re.compile(r"^#{1,6}\s+.*Risk\s+Flags", re.MULTILINE)),
]


def validate_template(filepath: Path) -> list[str]:
    """Validate a single template file. Returns a list of failure messages."""
    content = filepath.read_text(encoding="utf-8")
    failures: list[str] = []

    for name, message, pattern in REQUIRED_CHECKS:
        if not pattern.search(content):
            failures.append(message)

    return failures


def main() -> int:
    repo_root = Path(__file__).resolve().parent.parent
    templates_dir = repo_root / "templates"

    if not templates_dir.is_dir():
        print(f"Templates directory not found: {templates_dir}")
        return 1

    template_files = sorted(templates_dir.rglob("*.md"))

    if not template_files:
        print("No template files found in templates/.")
        return 0

    passed = 0
    failed = 0

    for filepath in template_files:
        relative = filepath.relative_to(repo_root)
        failures = validate_template(filepath)

        if not failures:
            print(f"  PASS  {relative}")
            passed += 1
        else:
            print(f"  FAIL  {relative}")
            for failure in failures:
                print(f"        - {failure}")
            failed += 1

    print(f"\nValidation summary: {passed} passed, {failed} failed out of {passed + failed} templates.")

    return 1 if failed > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
