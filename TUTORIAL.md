# kindle2md: Reproducible Tutorial

## Prerequisites
- Python 3.10+
- Git

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/Femirins/kindle-highlights-to-markdown.git
   cd kindle-highlights-to-markdown
   ```

2. Install dependencies:
   ```bash
   pip install -e .
   ```

## Usage
1. Prepare `My Clippings.txt` (e.g., from your Kindle).
2. Run the script:
   ```bash
   kindle2md --input "My Clippings.txt" --output notes.md --format obsidian
   ```

3. Check the output:
   ```bash
   cat notes.md
   ```

## Example
```bash
# Mock input
echo -e "The Pragmatic Programmer (Andrew Hunt)\n- Your Highlight on page 42 | Location 123-124\nThis is a highlight.\n\n==========\nClean Code (Robert Martin)\n- Your Highlight on page 100 | Location 456-457\nAnother highlight.\n" > input.txt

# Run the script
kindle2md --input input.txt --output output.md --format obsidian

# Output
cat output.md
```