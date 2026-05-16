# Kindle Highlights to Markdown/Notion/Anki

Convert your Kindle highlights (`My Clippings.txt`) into structured, searchable formats for Obsidian, Notion, and Anki.

## Features
- **Markdown Export**: Obsidian-compatible `.md` files with YAML frontmatter.
- **Anki Export**: CSV import format for spaced repetition.
- **Tagging**: Auto-tag highlights by book title.
- **Flexible Parsing**: Handles highlights, notes, and bookmarks.

## Installation
```bash
pip install pyyaml
```

## Usage
```bash
python3 kindle_highlights.py --input "My Clippings.txt" --output_dir ./output --format markdown
```

### Options
| Argument       | Description                                      |
|----------------|--------------------------------------------------|
| `--input`      | Path to `My Clippings.txt` (required)            |
| `--output_dir` | Output directory (default: `./output`)           |
| `--format`     | Export format: `markdown`, `anki`, or `notion`   |
| `--notion_token`| Notion API token (required for Notion export)    |
| `--database_id` | Notion database ID (required for Notion export)  |

## Example Output
### Markdown
```markdown
---
title: The Lean Startup
author: Eric Ries
tags: [the_lean_startup]
---

# The Lean Startup

**Author:** Eric Ries

## Location 123
**Added on:** 2025-05-10 14:30:22

The fundamental activity of a startup is to turn ideas into products...
```

### Anki CSV
```csv
Book,Highlight,Location,Tags
The Lean Startup,"If you cannot fail, you cannot learn.",456,the_lean_startup
```

## Technical Architecture
- **Parser**: Regex-based extraction of title, author, metadata, and highlight.
- **Tagger**: Auto-tags highlights by book title (customizable).
- **Exporters**: Modular design for new formats (e.g., Logseq, Roam).

## Limitations
- Notion export requires manual API setup (placeholder in code).
- Multi-language support depends on Kindle's clippings format.

## License
MIT