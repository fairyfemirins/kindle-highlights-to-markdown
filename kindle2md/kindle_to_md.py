#!/usr/bin/env python3
"""
Kindle Highlights to Markdown Converter
----------------------------------------
Converts Kindle's "My Clippings.txt" file into structured Markdown notes.

Usage:
    python3 kindle_to_md.py "My Clippings.txt" output.md
"""

import re
import sys
from datetime import datetime


def parse_clippings(file_path):
    """Parse Kindle's "My Clippings.txt" file into a structured format."""
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        content = file.read()
    
    # Split into individual clippings
    clippings = re.split(r'==========\n', content)
    parsed_clippings = []
    
    for clipping in clippings:
        if not clipping.strip():
            continue
        
        # Extract book title, metadata, and highlight
        lines = clipping.strip().split('\n')
        if len(lines) < 3:
            continue
        
        book_title = lines[0].strip()
        metadata = lines[1].strip()
        highlight = '\n'.join(lines[3:]).strip()
        
        # Parse metadata
        metadata_pattern = r'-(.*?) \| Added on (.*?)$'
        match = re.search(metadata_pattern, metadata)
        if not match:
            continue
        
        clipping_type = match.group(1).strip()
        date_added = match.group(2).strip()
        
        parsed_clippings.append({
            'book_title': book_title,
            'clipping_type': clipping_type,
            'date_added': date_added,
            'highlight': highlight
        })
    
    return parsed_clippings


def generate_markdown(clippings, output_path):
    """Generate Markdown from parsed clippings."""
    with open(output_path, 'w', encoding='utf-8') as file:
        for clipping in clippings:
            book_title = clipping['book_title']
            clipping_type = clipping['clipping_type']
            date_added = clipping['date_added']
            highlight = clipping['highlight']
            
            # Write book header
            file.write(f"# {book_title}\n\n")
            
            # Write clipping metadata
            file.write(f"> **{clipping_type}** | Added on {date_added}\n\n")
            
            # Write highlight as a blockquote
            file.write(f"> {highlight}\n\n")
            
            # Separator
            file.write("---\n\n")


def main():
    if len(sys.argv) != 3:
        print("Usage: python3 kindle_to_md.py <input_file> <output_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    clippings = parse_clippings(input_file)
    generate_markdown(clippings, output_file)
    print(f"Successfully converted {len(clippings)} clippings to {output_file}")


if __name__ == "__main__":
    main()