#!/usr/bin/env python3
"""
Kindle Highlights to Markdown (kindlemd)

Convert Kindle 'My Clippings.txt' to Markdown.
Usage:
  kindlemd --input "My Clippings.txt" --output "output.md" [--group-by-book] [--exclude-notes]
"""

import re
import click
from pathlib import Path
from typing import List, Dict, Optional


def parse_clippings(input_path: str) -> List[Dict]:
    """Parse Kindle 'My Clippings.txt' into a list of entries."""
    with open(input_path, 'r', encoding='utf-8-sig') as f:
        content = f.read()
    
    # Split entries by "==========" delimiter
    entries = content.split('==========')
    parsed_entries = []
    
    for entry in entries:
        entry = entry.strip()
        if not entry:
            continue
        
        # Extract title, author, location, date, and content
        lines = entry.split('\n')
        if len(lines) < 4:
            continue
        
        title_author = lines[0].strip()
        metadata = lines[1].strip()
        content = '\n'.join(lines[3:]).strip()
        
        # Parse title and author
        title_match = re.match(r'^(.*?)(?: \()?(.*?)(?:\()?$', title_author)
        title = title_match.group(1).strip() if title_match else title_author
        author = title_match.group(2).strip() if title_match and title_match.group(2) else "Unknown"
        
        # Parse location and date
        location_match = re.search(r'Location (\d+-\d+|\d+)', metadata)
        location = location_match.group(1) if location_match else "Unknown"
        
        date_match = re.search(r'Added on (.+)', metadata)
        date = date_match.group(1) if date_match else "Unknown"
        
        parsed_entries.append({
            'title': title,
            'author': author,
            'location': location,
            'date': date,
            'content': content
        })
    
    return parsed_entries


def group_by_book(entries: List[Dict]) -> Dict:
    """Group entries by book title."""
    grouped = {}
    for entry in entries:
        key = (entry['title'], entry['author'])
        if key not in grouped:
            grouped[key] = []
        grouped[key].append(entry)
    return grouped


def generate_markdown(entries: List[Dict], group_by_book: bool = False, exclude_notes: bool = False) -> str:
    """Generate Markdown from parsed entries."""
    if exclude_notes:
        entries = [e for e in entries if not e['content'].startswith('Note:')]
    
    if group_by_book:
        grouped = group_by_book(entries)
        markdown = ""
        for (title, author), book_entries in grouped.items():
            markdown += f"# {title}\n"
            markdown += f"**Author**: {author}\n\n"
            for entry in book_entries:
                markdown += f"- **Location {entry['location']}** (Added on {entry['date']})\n"
                markdown += f"  > {entry['content']}\n\n"
        return markdown
    else:
        markdown = ""
        for entry in entries:
            markdown += f"# {entry['title']}\n"
            markdown += f"**Author**: {entry['author']}\n"
            markdown += f"**Location**: {entry['location']} (Added on {entry['date']})\n\n"
            markdown += f"> {entry['content']}\n\n"
            markdown += "---\n\n"
        return markdown


@click.command()
@click.option('--input', '-i', required=True, type=click.Path(exists=True), help='Path to Kindle "My Clippings.txt"')
@click.option('--output', '-o', required=True, type=click.Path(), help='Output Markdown file path')
@click.option('--group-by-book', is_flag=True, help='Group highlights by book')
@click.option('--exclude-notes', is_flag=True, help='Exclude notes from output')
def main(input: str, output: str, group_by_book: bool = False, exclude_notes: bool = False):
    """Convert Kindle highlights to Markdown."""
    entries = parse_clippings(input)
    markdown = generate_markdown(entries, group_by_book, exclude_notes)
    
    with open(output, 'w', encoding='utf-8') as f:
        f.write(markdown)
    
    click.echo(f"✅ Converted {len(entries)} highlights to Markdown: {output}")


if __name__ == '__main__':
    main()