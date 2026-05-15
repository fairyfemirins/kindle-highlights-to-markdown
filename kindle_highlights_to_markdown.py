#!/usr/bin/env python3

"""
Kindle Highlights to Markdown

A CLI tool to convert Kindle's `My Clippings.txt` file into structured Markdown, JSON, or Obsidian-compatible notes.
"""

import argparse
import re
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional


class KindleHighlight:
    """Represents a single Kindle highlight or note."""

    def __init__(
        self,
        title: str,
        author: str,
        content: str,
        location: Optional[str] = None,
        page: Optional[str] = None,
        date: Optional[str] = None,
        highlight_type: str = "highlight",
    ):
        self.title = title.strip()
        self.author = author.strip()
        self.content = content.strip()
        self.location = location.strip() if location else None
        self.page = page.strip() if page else None
        self.date = date.strip() if date else None
        self.highlight_type = highlight_type.strip().lower()

    def to_markdown(self) -> str:
        """Convert the highlight to Markdown format."""
        metadata = []
        if self.location:
            metadata.append(f"Location: {self.location}")
        if self.page:
            metadata.append(f"Page: {self.page}")
        if self.date:
            metadata.append(f"Date: {self.date}")

        metadata_str = " | ".join(metadata) if metadata else ""
        header = f"## {self.content}"
        if metadata_str:
            header += f" \n_{metadata_str}_"

        return header

    def to_dict(self) -> Dict:
        """Convert the highlight to a dictionary."""
        return {
            "title": self.title,
            "author": self.author,
            "content": self.content,
            "location": self.location,
            "page": self.page,
            "date": self.date,
            "type": self.highlight_type,
        }


def parse_clippings(file_path: str) -> List[KindleHighlight]:
    """Parse a Kindle `My Clippings.txt` file and extract highlights."""
    with open(file_path, "r", encoding="utf-8-sig") as file:
        content = file.read()

    # Split into entries using the separator
    entries = re.split(r"==========", content)
    highlights = []

    for entry in entries:
        entry = entry.strip()
        if not entry:
            continue

        # Parse title, author, and metadata
        lines = entry.split("\n")
        if len(lines) < 3:
            continue

        title_author_line = lines[0].strip()
        metadata_line = lines[1].strip()
        content = "\n".join(lines[2:]).strip()

        # Extract title and author
        title_author_match = re.match(r"^(.*?)(?: \()(.*)(?:)\)?$", title_author_line)
        if not title_author_match:
            # Fallback: Assume the entire line is the title and author is unknown
            title = title_author_line
            author = "Unknown"
        else:
            title = title_author_match.group(1)
            author = title_author_match.group(2).rstrip(")")

        # Extract metadata (location, page, date, type)
        metadata_match = re.match(
            r"^- Your (Highlight|Note|Bookmark) (?:on|at) (?:Location|page) (\d+)(?:-(\d+))?(?: \| (.*))?$",
            metadata_line,
        )
        if not metadata_match:
            continue

        highlight_type = metadata_match.group(1)
        location = metadata_match.group(2)
        page = None
        date = None
        raw_metadata = metadata_match.group(3)

        # Parse location/page
        if "page" in metadata_line:
            page = location
            location = None
        elif metadata_match.group(3) and "-" in metadata_match.group(2):
            # Handle location ranges (e.g., 123-124)
            location = metadata_match.group(2)

        # Parse date
        if raw_metadata:
            date_match = re.search(r"Added on (.*)$", raw_metadata)
            if date_match:
                date = date_match.group(1).strip()

        highlights.append(
            KindleHighlight(
                title=title,
                author=author,
                content=content,
                location=location,
                page=page,
                date=date,
                highlight_type=highlight_type,
            )
        )

    return highlights


def export_to_markdown(highlights: List[KindleHighlight], output_path: str) -> None:
    """Export highlights to a Markdown file."""
    with open(output_path, "w", encoding="utf-8") as file:
        # Group by book
        books = {}
        for highlight in highlights:
            if highlight.title not in books:
                books[highlight.title] = []
            books[highlight.title].append(highlight)

        # Write each book's highlights
        for title, book_highlights in books.items():
            file.write(f"# {title}\n\n")
            for highlight in book_highlights:
                file.write(highlight.to_markdown() + "\n\n")


def export_to_json(highlights: List[KindleHighlight], output_path: str) -> None:
    """Export highlights to a JSON file."""
    with open(output_path, "w", encoding="utf-8") as file:
        json.dump([highlight.to_dict() for highlight in highlights], file, indent=2, ensure_ascii=False)


def export_to_obsidian(highlights: List[KindleHighlight], output_dir: Path) -> None:
    """Export highlights to Obsidian-compatible Markdown files."""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Group by book
    books = {}
    for highlight in highlights:
        if highlight.title not in books:
            books[highlight.title] = []
        books[highlight.title].append(highlight)

    # Write each book's highlights to a separate file
    for title, book_highlights in books.items():
        safe_title = "".join(c if c.isalnum() else "_" for c in title)
        output_path = output_dir / f"{safe_title}.md"
        with open(output_path, "w", encoding="utf-8") as file:
            file.write(f"---\ntag: kindle/highlights\nauthor: {book_highlights[0].author}\n---\n\n")
            file.write(f"# {title}\n\n")
            for highlight in book_highlights:
                file.write(highlight.to_markdown() + "\n\n")


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(description="Convert Kindle highlights to Markdown, JSON, or Obsidian notes.")
    parser.add_argument("--input", required=True, help="Path to the Kindle `My Clippings.txt` file.")
    parser.add_argument("--output", required=True, help="Output file path (for Markdown/JSON) or directory (for Obsidian).")
    parser.add_argument(
        "--format",
        required=True,
        choices=["markdown", "json", "obsidian"],
        help="Output format: markdown, json, or obsidian.",
    )
    args = parser.parse_args()

    highlights = parse_clippings(args.input)

    if args.format == "markdown":
        export_to_markdown(highlights, args.output)
    elif args.format == "json":
        export_to_json(highlights, args.output)
    elif args.format == "obsidian":
        export_to_obsidian(highlights, Path(args.output))

    print(f"Successfully exported {len(highlights)} highlights to {args.output}")


if __name__ == "__main__":
    main()