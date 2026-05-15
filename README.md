# Kindle Highlights to Markdown

A CLI tool to convert Kindle highlights from `My Clippings.txt` to Markdown files.

## Features
- Parse `My Clippings.txt` into structured data.
- Convert highlights to Markdown with proper formatting (headers, blockquotes, metadata).
- Batch processing for all highlights.
- Custom output directory.

## Installation
```bash
pip install -r requirements.txt
```

## Usage
```bash
python -m src.cli /path/to/My\ Clippings.txt --output /path/to/output
```

## Example Output
```markdown
# The Pragmatic Programmer: Your Journey to Mastery
**Author:** David Thomas
---

> This is a test highlight.

**Location:** 123-124
---
```

## License
MIT