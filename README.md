<<<<<<< HEAD
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
=======
# Kindle Highlights to Markdown Converter

A tool to convert Kindle's "My Clippings.txt" file into structured Markdown notes for easy integration into note-taking systems or blogs.

## Features
- Parses `My Clippings.txt` into book titles, highlights, notes, and metadata.
- Converts highlights into clean Markdown with blockquotes and metadata.
- Supports Unicode and special characters.

## Usage
### Prerequisites
- Python 3.6+

### Installation
Clone the repository:
```bash
git clone https://github.com/Femirins/kindle-highlights-to-markdown.git
cd kindle-highlights-to-markdown
```

### Convert Clippings
```bash
python3 kindle_to_md.py "My Clippings.txt" output.md
```

### Example
**Input (`My Clippings.txt`):**
```
The Pragmatic Programmer: Your Journey to Mastery (Andrew Hunt)
- Your Highlight on page 123 | Added on Tuesday, May 14, 2026 9:28:25 PM

The most important thing is to **think** about what you're doing.\n==========
```

**Output (`output.md`):**
```markdown
# The Pragmatic Programmer: Your Journey to Mastery (Andrew Hunt)

> **Your Highlight on page 123** | Added on Tuesday, May 14, 2026 9:28:25 PM

> The most important thing is to **think** about what you're doing.

---
```

## Technical Architecture
### Parsing Logic
1. **Splitting Clippings:** The `My Clippings.txt` file is split into individual clippings using the `==========` delimiter.
2. **Metadata Extraction:** Each clipping is parsed to extract:
   - Book title
   - Clipping type (highlight, note, or bookmark)
   - Date added
   - Highlight or note text
3. **Markdown Generation:** The parsed data is converted into Markdown with:
   - Book titles as headers (`#`)
   - Metadata as bold text (`** **`)
   - Highlights/notes as blockquotes (`> `)

### Error Handling
- Skips malformed clippings (e.g., missing metadata or text).
- Handles Unicode and special characters using `utf-8-sig` encoding.

## License
This project is licensed under the **MIT License**.
>>>>>>> 7ddfe3b9c00c3a0d121e53f424d0e19313a47963
## Note\nDue to rebase conflicts, this repository cannot be automatically synchronized. Manual intervention required.
