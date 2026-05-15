import sys
import os
import pytest
from pathlib import Path

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from kindle_highlights import KindleHighlight, parse_clippings


def test_parse_clippings():
    """Test parsing of My Clippings.txt."""
    highlights = parse_clippings("tests/mock_clippings.txt")
    
    # Check first book
    assert "The Pragmatic Programmer: Your Journey to Mastery" in highlights
    assert len(highlights["The Pragmatic Programmer: Your Journey to Mastery"]) == 1
    assert highlights["The Pragmatic Programmer: Your Journey to Mastery"][0].book == "The Pragmatic Programmer: Your Journey to Mastery"
    assert highlights["The Pragmatic Programmer: Your Journey to Mastery"][0].author == "David Thomas"
    assert highlights["The Pragmatic Programmer: Your Journey to Mastery"][0].text == "This is a test highlight."
    assert highlights["The Pragmatic Programmer: Your Journey to Mastery"][0].location == "123-124"
    
    # Check second book
    assert "Atomic Habits" in highlights
    assert len(highlights["Atomic Habits"]) == 1
    assert highlights["Atomic Habits"][0].book == "Atomic Habits"
    assert highlights["Atomic Habits"][0].author == "James Clear"
    assert highlights["Atomic Habits"][0].text == "Another test highlight."
    assert highlights["Atomic Habits"][0].location == "42"