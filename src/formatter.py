# formatter.py
from typing import List
from .parser import Highlight


def to_markdown(highlights: List[Highlight], output_dir: str = "output") -> None:
    """Convert a list of Highlight objects to Markdown files in the specified directory."""
    import os
    from pathlib import Path

    # Create output directory if it doesn't exist
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    # Group highlights by book title
    books = {}
    for highlight in highlights:
        if highlight.book_title not in books:
            books[highlight.book_title] = []
        books[highlight.book_title].append(highlight)

    # Write each book's highlights to a separate Markdown file
    for book_title, book_highlights in books.items():
        # Sanitize filename
        filename = "".join(c if c.isalnum() else "_" for c in book_title).strip("_") + ".md"
        filepath = os.path.join(output_dir, filename)

        with open(filepath, 'w', encoding='utf-8') as file:
            # Write book metadata
            file.write(f"# {book_title}\n")
            file.write(f"**Author:** {book_highlights[0].author}\n\n")
            file.write("---\n\n")

            # Write highlights
            for highlight in book_highlights:
                file.write(f"> {highlight.text}\n\n")
                if highlight.location:
                    file.write(f"**Location:** {highlight.location}\n\n")
                if highlight.date:
                    file.write(f"**Date:** {highlight.date}\n\n")
                file.write("---\n\n")