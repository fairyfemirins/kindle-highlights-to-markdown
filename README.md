# Kindle Highlights to Markdown

A CLI tool to parse Kindle highlights (`My Clippings.txt`) and export them to Markdown for Obsidian, Notion, or blogging.

## Features
- Parse `My Clippings.txt` into structured data.
- Export highlights to Markdown (one file per book).
- Filter by book, date, or highlight type.
- Deduplicate identical highlights.
- Zero dependencies (single-file executable).

## Installation
```bash
pip install kindle-highlights-to-markdown
```

## Usage
```bash
kindle-highlights --input "My Clippings.txt" --output "~/notes/kindle/"
```

## Example Output
```markdown
# The Pragmatic Programmer
**Author**: Andrew Hunt, David Thomas
**Date**: 2026-05-15

## Highlights
- > The cat ate my source code.
  *Location: 1234 | Added: 2026-05-10*

- > Programming is a craft.
  *Location: 5678 | Added: 2026-05-12* | #philosophy*
```

## License
MIT