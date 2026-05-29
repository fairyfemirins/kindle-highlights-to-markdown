# Kindle Highlights to Markdown (kindlemd)

Convert Kindle `My Clippings.txt` to Markdown with one command.

![GitHub License](https://img.shields.io/github/license/femirins/kindle-highlights-to-markdown)
![GitHub Repo stars](https://img.shields.io/github/stars/femirins/kindle-highlights-to-markdown)

## Features
- Convert Kindle highlights to Markdown.
- Group by book (`--group-by-book`).
- Exclude notes (`--exclude-notes`).
- Preserve location, date, and content.

## Installation
```bash
pip install click markdown
```

## Usage
```bash
python3 kindlemd.py --input "My Clippings.txt" --output "output.md" [--group-by-book] [--exclude-notes]
```

### Example
**Input (`My Clippings.txt`)**:
```
The Pragmatic Programmer (Andrew Hunt)
- Your Highlight on Location 123-124 | Added on Friday, May 29, 2026 11:26 AM

Debugging is twice as hard as writing the code in the first place.
==========
The Pragmatic Programmer (Andrew Hunt)
- Your Note on Location 125 | Added on Friday, May 29, 2026 11:27 AM

TODO: Read Chapter 3
```

**Command**:
```bash
python3 kindlemd.py --input "My Clippings.txt" --output "output.md" --group-by-book --exclude-notes
```

**Output (`output.md`)**:
```markdown
# The Pragmatic Programmer
**Author**: Andrew Hunt

- **Location 123-124** (Added on Friday, May 29, 2026 11:26 AM)
  > Debugging is twice as hard as writing the code in the first place.
```

## Technical Architecture
- **Parser**: Splits `My Clippings.txt` by `==========` delimiter.
- **Metadata Extraction**: Uses regex to extract title, author, location, date, and content.
- **Markdown Generation**: Supports grouping and note exclusion.

## License
MIT# Note

This repository is published under `fairyfemirins` due to GitHub namespace restrictions. A transfer to `Femirins` is pending.

## Transfer Instructions

To request a transfer:
1. Open an issue in this repository.
2. Contact `@Femirins` on GitHub.

### Manual Transfer Process
1. Navigate to: [https://github.com/fairyfemirins/kindle-highlights-to-markdown/settings](https://github.com/fairyfemirins/kindle-highlights-to-markdown/settings)
2. Under "Danger Zone", select "Transfer ownership".
3. Enter the target namespace (`Femirins`) and confirm.
