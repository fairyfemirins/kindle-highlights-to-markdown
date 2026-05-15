# parser.py
import re
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Highlight:
    book_title: str
    author: str
    text: str
    location: Optional[str] = None
    page: Optional[str] = None
    date: Optional[str] = None


def parse_clippings(file_path: str) -> List[Highlight]:
    """Parse Kindle's My Clippings.txt file into a list of Highlight objects."""
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        content = file.read()

    # Split entries by "==========" separator
    entries = re.split(r'==========\r?\n', content)
    highlights = []

    for entry in entries:
        if not entry.strip():
            continue

        # Parse book title and author
        title_author_match = re.match(r'^(.*?)\((.*?)\)$', entry.split('\n')[0].strip())
        if not title_author_match:
            continue
        book_title, author = title_author_match.groups()

        # Parse metadata (location, page, date)
        metadata_match = re.search(r'- Your (?:Highlight|Note|Bookmark) (?:on|at) (?:Location|Page) (\d+)(?:-(\d+))?(?: \| .*?(\d{1,2} \w+ \d{4}))?', entry)
        if not metadata_match:
            continue
        location, end_location, date = metadata_match.groups()
        location = f"{location}-{end_location}" if end_location else location

        # Extract highlight text
        text_match = re.search(r'\n\n(.*)', entry, re.DOTALL)
        if not text_match:
            continue
        text = text_match.group(1).strip()

        highlights.append(
            Highlight(
                book_title=book_title,
                author=author,
                text=text,
                location=location,
                date=date
            )
        )

    return highlights