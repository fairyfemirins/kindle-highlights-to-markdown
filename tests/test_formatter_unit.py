# tests/test_formatter.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.parser import Highlight
from src.formatter import to_markdown
import tempfile
import shutil


def test_to_markdown():
    highlights = [
        Highlight(
            book_title="Test Book",
            author="Test Author",
            text="Test highlight.",
            location="123"
        )
    ]

    # Use a temporary directory for output
    with tempfile.TemporaryDirectory() as temp_dir:
        to_markdown(highlights, temp_dir)
        output_file = os.path.join(temp_dir, "Test_Book.md")
        assert os.path.exists(output_file)
        
        with open(output_file, 'r', encoding='utf-8') as file:
            content = file.read()
            assert "# Test Book" in content
            assert "Test Author" in content
            assert "> Test highlight." in content
            assert "**Location:** 123" in content