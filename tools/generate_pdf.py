#!/usr/bin/env python3
"""Convert a markdown file to PDF using weasyprint.

Professional CSS styling with navy header bar, gray striped tables,
page numbers in footer, and "Elder Command Center" footer text.

Usage:
    python tools/generate_pdf.py <input.md> [output.pdf]
    python tools/generate_pdf.py --batch
"""

import argparse
import sys
from pathlib import Path

import markdown
from weasyprint import HTML

CSS_STYLES = """
@page {
    size: letter;
    margin: 1in 0.75in 1in 0.75in;

    @top-left {
        content: "";
        display: block;
        height: 4px;
        background-color: #1a237e;
        width: 100%;
    }

    @bottom-center {
        content: "Elder Command Center";
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        font-size: 9pt;
        color: #666666;
    }

    @bottom-right {
        content: "Page " counter(page) " of " counter(pages);
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        font-size: 9pt;
        color: #666666;
    }
}

body {
    font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    font-size: 11pt;
    line-height: 1.6;
    color: #222222;
}

h1 {
    color: #1a237e;
    font-size: 22pt;
    border-bottom: 3px solid #1a237e;
    padding-bottom: 6px;
    margin-top: 0;
}

h2 {
    color: #1a237e;
    font-size: 16pt;
    border-bottom: 1px solid #cccccc;
    padding-bottom: 4px;
    margin-top: 24px;
}

h3 {
    color: #333333;
    font-size: 13pt;
    margin-top: 18px;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin: 16px 0;
    font-size: 10pt;
}

thead tr {
    background-color: #1a237e;
    color: #ffffff;
}

th {
    padding: 8px 10px;
    text-align: left;
    font-weight: 600;
}

td {
    padding: 6px 10px;
    border-bottom: 1px solid #dddddd;
}

tbody tr:nth-child(even) {
    background-color: #f5f5f5;
}

tbody tr:nth-child(odd) {
    background-color: #ffffff;
}

code {
    font-family: 'Courier New', Courier, monospace;
    background-color: #f0f0f0;
    padding: 2px 4px;
    border-radius: 3px;
    font-size: 10pt;
}

pre {
    background-color: #f0f0f0;
    padding: 12px;
    border-radius: 4px;
    overflow-x: auto;
    font-size: 9pt;
    line-height: 1.4;
}

pre code {
    background-color: transparent;
    padding: 0;
}

blockquote {
    border-left: 4px solid #1a237e;
    margin: 16px 0;
    padding: 8px 16px;
    color: #555555;
    background-color: #f9f9f9;
}

ul, ol {
    margin: 8px 0;
    padding-left: 24px;
}

li {
    margin-bottom: 4px;
}

hr {
    border: none;
    border-top: 2px solid #1a237e;
    margin: 24px 0;
}
"""

MARKDOWN_EXTENSIONS = ["tables", "fenced_code", "toc", "attr_list", "md_in_html"]


def convert_md_to_pdf(input_path: Path, output_path: Path) -> None:
    """Convert a single markdown file to PDF."""
    md_content = input_path.read_text(encoding="utf-8")
    html_body = markdown.markdown(md_content, extensions=MARKDOWN_EXTENSIONS)

    full_html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <style>{CSS_STYLES}</style>
</head>
<body>
{html_body}
</body>
</html>"""

    HTML(string=full_html).write_pdf(str(output_path))


def main() -> int:
    parser = argparse.ArgumentParser(description="Convert markdown files to PDF with professional styling.")
    parser.add_argument("input", nargs="?", help="Input markdown file path.")
    parser.add_argument("output", nargs="?", help="Output PDF file path (default: same name with .pdf extension).")
    parser.add_argument("--batch", action="store_true", help="Convert all .md files in outputs/reports/.")
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parent.parent

    if args.batch:
        reports_dir = repo_root / "outputs" / "reports"
        if not reports_dir.is_dir():
            print(f"Reports directory not found: {reports_dir}")
            return 1

        md_files = sorted(reports_dir.glob("*.md"))
        if not md_files:
            print("No .md files found in outputs/reports/.")
            return 0

        errors = 0
        for md_file in md_files:
            pdf_file = md_file.with_suffix(".pdf")
            try:
                convert_md_to_pdf(md_file, pdf_file)
                print(f"  Generated  {pdf_file.relative_to(repo_root)}")
            except Exception as exc:
                print(f"  Error      {md_file.relative_to(repo_root)}: {exc}")
                errors += 1

        print(f"\nBatch complete: {len(md_files) - errors} generated, {errors} errors.")
        return 1 if errors > 0 else 0

    if not args.input:
        parser.error("Either provide an input file or use --batch.")

    input_path = Path(args.input).resolve()
    if not input_path.is_file():
        print(f"Input file not found: {input_path}")
        return 1

    if args.output:
        output_path = Path(args.output).resolve()
    else:
        output_path = input_path.with_suffix(".pdf")

    try:
        convert_md_to_pdf(input_path, output_path)
        print(f"Generated: {output_path}")
    except Exception as exc:
        print(f"Error generating PDF: {exc}")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
