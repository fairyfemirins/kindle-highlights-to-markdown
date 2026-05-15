# tests/test_parser.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.parser import parse_clippings, Highlight


def test_parse_clippings():
    highlights = parse_clippings("tests/mock_clippings.txt")
    assert len(highlights) == 2
    assert highlights[0].book_title == "The Pragmatic Programmer: Your Journey to Mastery"
    assert highlights[0].author == "David Thomas"
    assert highlights[0].text == "This is a test highlight."
    assert highlights[0].location == "123-124"
    assert highlights[1].book_title == "Atomic Habits"
    assert highlights[1].author == "James Clear"
    assert highlights[1].text == "Another test highlight."
    assert highlights[1].page == "42"