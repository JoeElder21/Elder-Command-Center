#!/usr/bin/env python3
"""Generate table of contents from markdown headings.

Supports --inject flag to insert the TOC into the file after the first H1 heading.

Usage:
    python tools/generate_toc.py <file.md>
    python tools/generate_toc.py <file.md> --inject
"""

import argparse
import re
import sys
from pathlib import Path

HEADING_PATTERN = re.compile(r"^(#{1,6})\s+(.+)$", re.MULTILINE)

TOC_START_MARKER = "<!-- TOC START -->"
TOC_END_MARKER = "<!-- TOC END -->"


def slugify(text: str) -> str:
    """Convert heading text to a GitHub-style anchor slug."""
    slug = text.lower().strip()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"[\s]+", "-", slug)
    slug = re.sub(r"-+", "-", slug)
    return slug.strip("-")


def generate_toc(content: str) -> str:
    """Generate a markdown table of contents from headings in content."""
    # Strip any existing TOC block before scanning headings.
    stripped = re.sub(
        rf"{re.escape(TOC_START_MARKER)}.*?{re.escape(TOC_END_MARKER)}",
        "",
        content,
        flags=re.DOTALL,
    )

    # Skip headings inside fenced code blocks.
    in_code_block = False
    lines = stripped.split("\n")
    headings: list[tuple[int, str]] = []

    for line in lines:
        if line.strip().startswith("```"):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue
        match = HEADING_PATTERN.match(line)
        if match:
            level = len(match.group(1))
            text = match.group(2).strip()
            headings.append((level, text))

    if not headings:
        return ""

    # Find the minimum heading level to normalize indentation.
    min_level = min(level for level, _ in headings)
    toc_lines: list[str] = []

    for level, text in headings:
        indent = "  " * (level - min_level)
        anchor = slugify(text)
        toc_lines.append(f"{indent}- [{text}](#{anchor})")

    return "\n".join(toc_lines)


def inject_toc(content: str, toc: str) -> str:
    """Inject or replace TOC in the file content after the first H1 heading."""
    toc_block = f"{TOC_START_MARKER}\n\n## Table of Contents\n\n{toc}\n\n{TOC_END_MARKER}"

    # Replace existing TOC block if present.
    if TOC_START_MARKER in content:
        return re.sub(
            rf"{re.escape(TOC_START_MARKER)}.*?{re.escape(TOC_END_MARKER)}",
            toc_block,
            content,
            flags=re.DOTALL,
        )

    # Find the first H1 heading and insert TOC after it.
    h1_match = re.search(r"^# .+$", content, re.MULTILINE)
    if h1_match:
        insert_pos = h1_match.end()
        return content[:insert_pos] + "\n\n" + toc_block + "\n" + content[insert_pos:]

    # No H1 found; prepend the TOC.
    return toc_block + "\n\n" + content


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate table of contents from markdown headings.")
    parser.add_argument("file", help="Markdown file to process.")
    parser.add_argument("--inject", action="store_true", help="Insert TOC into the file after the first H1 heading.")
    args = parser.parse_args()

    filepath = Path(args.file).resolve()
    if not filepath.is_file():
        print(f"File not found: {filepath}")
        return 1

    content = filepath.read_text(encoding="utf-8")
    toc = generate_toc(content)

    if not toc:
        print("No headings found in file.")
        return 0

    if args.inject:
        updated = inject_toc(content, toc)
        filepath.write_text(updated, encoding="utf-8")
        print(f"TOC injected into {filepath}")
    else:
        print(toc)

    return 0


if __name__ == "__main__":
    sys.exit(main())
