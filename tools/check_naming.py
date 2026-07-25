#!/usr/bin/env python3
"""Enforce lowercase-with-hyphens naming for all .md files.

Rules:
  - All .md filenames must be lowercase-with-hyphens (e.g., my-document.md).
  - Template files (in templates/) must end with -template.md.

Prints violations and exits 1 if any are found.
"""

import re
import sys
from pathlib import Path

# Matches valid lowercase-with-hyphens filenames: letters, digits, hyphens only.
VALID_NAME_PATTERN = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*\.md$")

# Template files must end with -template.md.
TEMPLATE_SUFFIX = "-template.md"


def check_naming(repo_root: Path) -> list[str]:
    """Check all .md files for naming violations. Returns a list of violation messages."""
    violations: list[str] = []
    md_files = sorted(repo_root.rglob("*.md"))

    for filepath in md_files:
        relative = filepath.relative_to(repo_root)
        filename = filepath.name

        # Check lowercase-with-hyphens naming.
        if not VALID_NAME_PATTERN.match(filename):
            violations.append(f"  {relative} -- filename must be lowercase-with-hyphens (got '{filename}')")

        # Check template naming convention.
        if "templates" in relative.parts and not filename.endswith(TEMPLATE_SUFFIX):
            violations.append(f"  {relative} -- template files must end with '{TEMPLATE_SUFFIX}' (got '{filename}')")

    return violations


def main() -> int:
    repo_root = Path(__file__).resolve().parent.parent
    violations = check_naming(repo_root)

    if not violations:
        print("All .md files follow naming conventions.")
        return 0

    print("Naming violations found:\n")
    for violation in violations:
        print(violation)

    print(f"\n{len(violations)} violation(s) found.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
