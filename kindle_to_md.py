#!/usr/bin/env python3
"""
Kindle Highlights to Markdown
=============================

Parses Kindle's `My Clippings.txt` and exports highlights to Markdown files.
Supports custom templates and frontmatter for Obsidian/Logseq.

Usage:
  python kindle_to_md.py --input "My Clippings.txt" --output "output/"
"""

import argparse
import re
from pathlib import Path
from typing import Dict, List, Optional


class KindleHighlight:
    """Represents a single Kindle highlight."""
    def __init__(self, book_title: str, author: str, content: str, location: str, date: str):
        self.book_title = book_title.strip()
        self.author = author.strip()
        self.content = content.strip()
        self.location = location.strip()
        self.date = date.strip()

    def to_markdown(self, template: str = "default") -> str:
        """Convert highlight to Markdown using a template."""
        if template == "obsidian":
            return f"> [!quote] {self.content}\n> — *{self.book_title}* (Location {self.location})\n"
        elif template == "logseq":
            return f"- {self.content} #[[{self.book_title}]]\n"
        else:  # default
            return f"> {self.content}\n> — *{self.book_title}* (Location {self.location})\n"


def parse_clippings(file_path: Path) -> List[KindleHighlight]:
    """Parse Kindle's `My Clippings.txt` into a list of highlights."""
    with open(file_path, "r", encoding="utf-8-sig") as f:
        content = f.read()

    # Split into entries (Kindle uses "==========" as delimiter)
    entries = re.split(r"\n==========\n", content)
    highlights = []

    for entry in entries:
        if not entry.strip():
            continue

        # Regex to extract book title, author, content, location, and date
        pattern = r"^(.*?)\n-\sYour\sHighlight\son\s(?:page\s\d+\s\|\s)?Location\s(\d+-\d+|\d+)\s\|\sAdded\son\s(.*)\n\n(.*?)$"
        match = re.match(pattern, entry, re.DOTALL)
        if match:
            book_title, location, date, content = match.groups()
            # Extract author (last part in parentheses)
            author_match = re.search(r"\((.*?)\)$", book_title)
            author = author_match.group(1) if author_match else "Unknown"
            book_title = re.sub(r"\s*\(.*?\)$", "", book_title).strip()
            highlights.append(KindleHighlight(book_title, author, content, location, date))

    return highlights


def export_to_markdown(highlights: List[KindleHighlight], output_dir: Path, template: str = "default") -> None:
    """Export highlights to Markdown files, grouped by book."""
    output_dir.mkdir(parents=True, exist_ok=True)
    books: Dict[str, List[KindleHighlight]] = {}

    # Group by book title
    for highlight in highlights:
        if highlight.book_title not in books:
            books[highlight.book_title] = []
        books[highlight.book_title].append(highlight)

    # Write each book to a separate Markdown file
    for book_title, book_highlights in books.items():
        md_content = f"# {book_title}\n\n**Author:** {book_highlights[0].author}\n\n"
        for highlight in book_highlights:
            md_content += highlight.to_markdown(template) + "\n"

        # Sanitize filename
        safe_title = re.sub(r"[^a-zA-Z0-9\s-]", "", book_title).strip()
        safe_title = re.sub(r"\s+", "_", safe_title)
        output_path = output_dir / f"{safe_title}.md"
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(md_content)


def main():
    parser = argparse.ArgumentParser(description="Convert Kindle highlights to Markdown.")
    parser.add_argument("--input", type=Path, required=True, help="Path to Kindle's 'My Clippings.txt'")
    parser.add_argument("--output", type=Path, required=True, help="Output directory for Markdown files")
    parser.add_argument("--template", type=str, default="default", choices=["default", "obsidian", "logseq"], help="Markdown template (default, obsidian, logseq)")
    args = parser.parse_args()

    highlights = parse_clippings(args.input)
    export_to_markdown(highlights, args.output, args.template)
    print(f"Exported {len(highlights)} highlights to {args.output}")


if __name__ == "__main__":
    main()