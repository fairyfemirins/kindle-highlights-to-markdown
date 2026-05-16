#!/usr/bin/env python3
"""
Kindle Highlights to Markdown/Notion/Anki

Parses My Clippings.txt and exports highlights to:
- Markdown (Obsidian-compatible with YAML frontmatter)
- Notion (via API)
- Anki (CSV import format)

Usage:
  python3 kindle_highlights.py --input "My Clippings.txt" --output_dir ./output --format markdown
"""

import re
import argparse
from pathlib import Path
from datetime import datetime
import yaml
import csv
import os


class KindleHighlights:
    def __init__(self, input_path):
        self.input_path = input_path
        self.highlights = []
        self.books = set()

    def parse(self):
        """Parse My Clippings.txt into structured data."""
        with open(self.input_path, 'r', encoding='utf-8-sig') as f:
            content = f.read()

        # Split into entries (Kindle separates entries with "==========")
        entries = content.split('==========')
        for entry in entries:
            entry = entry.strip()
            if not entry:
                continue

            # Simplified regex to extract title, author, metadata, and highlight
            pattern = r"^(.*?) \((.*?)\)\r?\n- (.+?)\r?\n\r?\n([\s\S]+?)$"
            match = re.match(pattern, entry, re.DOTALL | re.MULTILINE)
            if not match:
                continue

            title, author, metadata, highlight = match.groups()
            timestamp = self._extract_timestamp(metadata)
            location = self._extract_location(metadata)

            self.highlights.append({
                'title': title.strip(),
                'author': author.strip(),
                'highlight': highlight.strip(),
                'location': location,
                'timestamp': timestamp,
                'tags': []
            })
            self.books.add(title.strip())

    def _extract_timestamp(self, metadata):
        """Extract timestamp from metadata."""
        pattern = r"Added on (.*?)$"
        match = re.search(pattern, metadata)
        if match:
            dt_str = match.group(1)
            try:
                return datetime.strptime(dt_str, '%A, %B %d, %Y %I:%M:%S %p')
            except ValueError:
                return None
        return None

    def _extract_location(self, metadata):
        """Extract location/page from metadata."""
        pattern = r"(?:location|loc|page|pos) (\d+)"
        match = re.search(pattern, metadata, re.IGNORECASE)
        return match.group(1) if match else "Unknown"

    def add_tags(self, tags):
        """Add tags to highlights (e.g., by book title)."""
        for highlight in self.highlights:
            highlight['tags'].extend(tags.get(highlight['title'], []))

    def export_markdown(self, output_dir):
        """Export highlights to Markdown files (Obsidian-compatible)."""
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        for book in self.books:
            book_highlights = [h for h in self.highlights if h['title'] == book]
            if not book_highlights:
                continue

            md_content = f"# {book}\n\n**Author:** {book_highlights[0]['author']}\n\n"
            for h in book_highlights:
                md_content += f"## Location {h['location']}\n"
                md_content += f"**Added on:** {h['timestamp'].strftime('%Y-%m-%d %H:%M:%S') if h['timestamp'] else 'Unknown'}\n"
                md_content += f"**Tags:** {', '.join(h['tags']) if h['tags'] else 'None'}\n\n"
                md_content += f"{h['highlight']}\n\n---\n\n"

            # Write to file with YAML frontmatter for Obsidian
            frontmatter = {
                'title': book,
                'author': book_highlights[0]['author'],
                'tags': list(set(sum([h['tags'] for h in book_highlights], []))),
                'created': datetime.now().strftime('%Y-%m-%d')
            }

            md_file = output_dir / f"{self._sanitize_filename(book)}.md"
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write('---\n')
                yaml.dump(frontmatter, f, allow_unicode=True)
                f.write('---\n\n')
                f.write(md_content)

    def export_notion(self, output_dir, notion_token, database_id):
        """Export highlights to Notion (placeholder)."""
        # TODO: Implement Notion API integration
        pass

    def export_anki(self, output_dir):
        """Export highlights to Anki-compatible CSV."""
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        csv_file = output_dir / "anki_highlights.csv"

        with open(csv_file, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Book', 'Highlight', 'Location', 'Tags'])
            for h in self.highlights:
                writer.writerow([
                    h['title'],
                    h['highlight'],
                    h['location'],
                    ', '.join(h['tags'])
                ])

    def _sanitize_filename(self, filename):
        """Sanitize filenames for use in paths."""
        return re.sub(r'[\\/*?:"<>|]', "_", filename)


def main():
    parser = argparse.ArgumentParser(description='Convert Kindle highlights to Markdown/Notion/Anki.')
    parser.add_argument('--input', required=True, help='Path to My Clippings.txt')
    parser.add_argument('--output_dir', default='./output', help='Output directory')
    parser.add_argument('--format', choices=['markdown', 'notion', 'anki'], required=True, help='Export format')
    parser.add_argument('--notion_token', help='Notion API token (required for Notion export)')
    parser.add_argument('--database_id', help='Notion database ID (required for Notion export)')
    args = parser.parse_args()

    # Parse highlights
    kh = KindleHighlights(args.input)
    kh.parse()

    # Add tags (example: tag by book title)
    tags = {book: [book.lower().replace(' ', '_')] for book in kh.books}
    kh.add_tags(tags)

    # Export
    if args.format == 'markdown':
        kh.export_markdown(args.output_dir)
    elif args.format == 'notion':
        if not args.notion_token or not args.database_id:
            raise ValueError("Notion token and database ID are required for Notion export.")
        kh.export_notion(args.output_dir, args.notion_token, args.database_id)
    elif args.format == 'anki':
        kh.export_anki(args.output_dir)

    print(f"Exported {len(kh.highlights)} highlights to {args.output_dir}")


if __name__ == '__main__':
    main()