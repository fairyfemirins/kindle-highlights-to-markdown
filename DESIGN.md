# kindle2md: Design Document

## 1. Problem Statement
Kindle users need a way to convert their highlights (`My Clippings.txt`) into structured markdown for note-taking apps like Obsidian, Notion, and Logseq. Existing tools are GUI-based or lack multi-format support.

## 2. Architecture
```
[My Clippings.txt] → [Parser] → [Exporter] → [Markdown]
```

### 2.1 Components
- **Parser**: Extracts highlights, metadata, and organizes them into `Book` and `Highlight` objects.
- **Exporter**: Uses Jinja2 templates to generate markdown for Obsidian, Notion, and Logseq.
- **CLI**: Provides a user-friendly interface for conversion.

### 2.2 Data Flow
1. Parse `My Clippings.txt` into `Book` objects.
2. Render markdown using Jinja2 templates.
3. Save output to a file.

## 3. Implementation Details
- **Parser**: Uses regex to split entries and extract metadata.
- **Exporter**: Jinja2 templates for Obsidian, Notion, and Logseq.
- **CLI**: Built with `click` for argument parsing.

## 4. Future Work
- Add support for more formats (e.g., Roam Research).
- Improve error handling for malformed `My Clippings.txt`.

## 5. License
MIT