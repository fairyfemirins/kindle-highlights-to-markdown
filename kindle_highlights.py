#!/usr/bin/env python3
"""
kindle-highlights-to-markdown: Parse Kindle highlights and export to Markdown.
"""

import re
import click
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Optional


class KindleHighlight:
    """Represents a single Kindle highlight or note."""

    def __init__(self, book: str, author: str, text: str, location: str, date: str, is_note: bool = False):
        self.book = book.strip()
        self.author = author.strip()
        self.text = text.strip()
        self.location = location
        try:
            self.date = datetime.strptime(date, "%A, %B %d, %Y %I:%M:%S %p")
        except ValueError:
            self.date = datetime.strptime(date, "%A, %B %d, %Y, %I:%M %p")
        self.is_note = is_note
        self.tags = self._extract_tags()

    def _extract_tags(self) -> List[str]:
        """Extract hashtags from highlight text."""
        return re.findall(r"#(\w+)", self.text)

    def to_markdown(self) -> str:
        """Convert highlight to Markdown format."""
        prefix = "> " if not self.is_note else ""
        tags = " " + " ".join(f"#{tag}" for tag in self.tags) if self.tags else ""
        return (
            f"{prefix}{self.text}{tags}\n"
            f"  *Location: {self.location} | Added: {self.date.strftime('%Y-%m-%d')}*"
        )


def parse_clippings(file_path: str) -> Dict[str, List[KindleHighlight]]:
    """Parse My Clippings.txt into a dictionary of {book_title: [highlights]}."""
    with open(file_path, "r", encoding="utf-8-sig") as f:
        content = f.read()

    # Kindle clippings format:
    # Book Title (Author)
    # - Your Highlight on Location 123-124 | Added on Friday, May 15, 2026, 2:49 PM
    # 
    # Highlight text
    # ======
    pattern = re.compile(
        r"^(.*?) \((.*?)\)\n"
        r"- Your (Highlight|Note) on (?:Location|page) (.*?) \| Added on (.*?)\n"
        r"\n(.*?)\n"
        r"======",
        re.MULTILINE | re.DOTALL,
    )

    highlights = {}
    for match in pattern.finditer(content):
        book, author, highlight_type, location, date, text = match.groups()
        is_note = highlight_type == "Note"
        highlight = KindleHighlight(book, author, text, location, date, is_note)
        if book not in highlights:
            highlights[book] = []
        highlights[book].append(highlight)

    return highlights


def export_to_markdown(highlights: Dict[str, List[KindleHighlight]], output_dir: str) -> None:
    """Export highlights to Markdown files (one per book)."""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    for book, book_highlights in highlights.items():
        # Sanitize filename
        safe_book = "".join(c for c in book if c.isalnum() or c in " _-").rstrip()
        output_file = output_path / f"{safe_book}.md"

        # Group by date (optional)
        book_highlights.sort(key=lambda h: h.date)

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(f"# {book}\n")
            f.write(f"**Author**: {book_highlights[0].author}\n")
            f.write(f"**Date**: {datetime.now().strftime('%Y-%m-%d')}\n\n")
            f.write("## Highlights\n")
            for highlight in book_highlights:
                f.write(highlight.to_markdown() + "\n\n")


@click.command()
@click.option("--input", "input_file", required=True, help="Path to My Clippings.txt")
@click.option("--output", "output_dir", required=True, help="Output directory for Markdown files")
def cli(input_file: str, output_dir: str) -> None:
    """CLI entry point."""
    highlights = parse_clippings(input_file)
    export_to_markdown(highlights, output_dir)
    click.echo(f"Exported {len(highlights)} books to {output_dir}")


if __name__ == "__main__":
    cli()