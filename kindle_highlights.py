#!/usr/bin/env python3
"""
Kindle Highlights to Markdown CLI

Parses Kindle's 'My Clippings.txt' and exports highlights/notes to Markdown.
Format: 

# Book Title (Author)

> Highlight/Note
> - Location 123 | Added on Friday, May 15, 2026

"""

import re
import argparse
from pathlib import Path
from typing import List, Dict, Optional


class KindleHighlight:
    """Represents a single highlight or note from Kindle."""

    def __init__(self, book_title: str, author: str, content: str, location: str, date: str, highlight_type: str):
        self.book_title = book_title.strip()
        self.author = author.strip()
        self.content = content.strip()
        self.location = location.strip()
        self.date = date.strip()
        self.type = highlight_type.strip()  # "Highlight" or "Note"

    def to_markdown(self) -> str:
        """Convert highlight/note to Markdown."""
        header = f"# {self.book_title} ({self.author})\n\n"
        body = f"> {self.content}\n> - {self.type} | Location {self.location} | Added on {self.date}\n\n"
        return header + body


def parse_clippings(file_path: Path) -> List[KindleHighlight]:
    """Parse 'My Clippings.txt' and return a list of highlights/notes."""
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        content = f.read()

    # Split into entries (separated by "==========")
    entries = re.split(r'\r?\n==========\r?\n', content)
    highlights = []

    for entry in entries:
        if not entry.strip():
            continue

        # Regex to extract metadata (flexible for "page X" or no page)
        pattern = r'^(.*?)\n(.*?)\n- (Your (Highlight|Note)( on page \d+)? \| Location (\d+-\d+|\d+) \| Added on (.*?))$'
        match = re.match(pattern, entry, re.MULTILINE | re.DOTALL)
        if not match:
            continue

        book_title = match.group(1)
        author = match.group(2)
        metadata = match.group(3)
        highlight_type = match.group(4)
        location = match.group(6)  # Updated group index
        date = match.group(7)      # Updated group index
        content = entry.split(metadata)[1].strip()

        highlights.append(
            KindleHighlight(
                book_title=book_title,
                author=author,
                content=content,
                location=location,
                date=date,
                highlight_type=highlight_type
            )
        )

    return highlights


def export_to_markdown(highlights: List[KindleHighlight], output_path: Path) -> None:
    """Export highlights to a Markdown file."""
    with open(output_path, 'w', encoding='utf-8') as f:
        # Group by book
        books: Dict[str, List[KindleHighlight]] = {}
        for h in highlights:
            if h.book_title not in books:
                books[h.book_title] = []
            books[h.book_title].append(h)

        # Write each book's highlights
        for book_title, book_highlights in books.items():
            f.write(book_highlights[0].to_markdown())


def main():
    parser = argparse.ArgumentParser(description='Convert Kindle highlights to Markdown.')
    parser.add_argument('input', type=Path, help='Path to My Clippings.txt')
    parser.add_argument('-o', '--output', type=Path, default='highlights.md', help='Output Markdown file')
    args = parser.parse_args()

    if not args.input.exists():
        raise FileNotFoundError(f"Input file not found: {args.input}")

    highlights = parse_clippings(args.input)
    export_to_markdown(highlights, args.output)
    print(f"Exported {len(highlights)} highlights to {args.output}")


if __name__ == '__main__':
    main()