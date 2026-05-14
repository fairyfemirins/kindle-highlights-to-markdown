# Kindle Highlights to Markdown

Convert Kindle's `My Clippings.txt` into **clean, organized Markdown** for Obsidian, Logseq, or any note-taking app.

![GitHub License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python Version](https://img.shields.io/badge/python-3.8+-green.svg)

---

## Features
✅ **Parses `My Clippings.txt`** (handles Kindle's non-standard encoding)
✅ **Groups highlights by book/author**
✅ **Exports to Markdown** with frontmatter (title, author, date)
✅ **Custom templates** for Obsidian/Logseq
✅ **CLI interface** for automation

---

## Installation
```bash
pip install -r requirements.txt  # (None needed for now)
```

---

## Usage
```bash
python kindle_to_md.py --input "My Clippings.txt" --output "output/" --template obsidian
```

### Templates
| Template  | Output Format                          |
|-----------|----------------------------------------|
| `default` | `> Quote`                              |
| `obsidian`| `> [!quote] Quote` (Obsidian callouts) |
| `logseq`  | `- Quote #[[Book Title]]`              |

---

## Example
**Input (`My Clippings.txt`):**
```text
The Psychology of Money (Morgan Housel)
- Your Highlight on Location 123-124 | Added on Thursday, May 14, 2026 08:16:23 PM

The most important part of every plan is planning on your plan not going according to plan.
```

**Output (`The_Psychology_of_Money.md`):**
```markdown
# The Psychology of Money

**Author:** Morgan Housel

> [!quote] The most important part of every plan is planning on your plan not going according to plan.
> — *The Psychology of Money* (Location 123-124)
```

---

## Technical Architecture
1. **Parser:** Uses regex to split Kindle's `==========` delimiter and extract metadata (title, author, location, date).
2. **Templates:** Supports pluggable Markdown templates via `KindleHighlight.to_markdown()`.
3. **Output:** Writes one `.md` file per book, sanitizing filenames for cross-platform compatibility.

---

## Limitations
- Does not support **notes** or **bookmarks** (highlights only).
- Assumes English-language clippings (regex may fail on non-Latin scripts).

---

## License
MIT © Femirins