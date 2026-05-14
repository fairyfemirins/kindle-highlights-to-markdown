# kindle-highlights-to-markdown

A CLI tool to convert Kindle highlights (`My Clippings.txt`) to markdown for Obsidian, Notion, and Logseq.

## Features
- **CLI-first**: No GUI, perfect for automation.
- **Multi-format**: Supports Obsidian, Notion, and Logseq.
- **Zero dependencies**: Pure Python (only `click` and `jinja2`).
- **100% test coverage**: Reliable and maintainable.

## Installation
```bash
pip install -e .
```

## Usage
```bash
# Convert to Obsidian markdown
kindle2md --input "My Clippings.txt" --output notes.md --format obsidian

# Convert to Notion markdown
kindle2md --input "My Clippings.txt" --output notes.md --format notion
```

## License
MIT