import pytest
from pathlib import Path
from kindle_highlights import parse_clippings, KindleHighlight


def test_parse_clippings():
    """Test parsing of 'My Clippings.txt'."""
    test_file = Path(__file__).parent / "test_clippings.txt"
    highlights = parse_clippings(test_file)
    
    # Should parse 3 entries
    assert len(highlights) == 3
    
    # First highlight
    assert highlights[0].book_title == "The Pragmatic Programmer"
    assert highlights[0].author == "Andrew Hunt; David Thomas"
    assert highlights[0].content == "This is a highlight from the book."
    assert highlights[0].location == "123-124"
    assert highlights[0].type == "Highlight"
    
    # Second entry (note)
    assert highlights[1].book_title == "The Pragmatic Programmer"
    assert highlights[1].type == "Note"
    assert highlights[1].content == "This is a note about the highlight."
    
    # Third highlight
    assert highlights[2].book_title == "Atomic Habits"
    assert highlights[2].author == "James Clear"
    assert highlights[2].content == "This is another highlight."


def test_export_markdown():
    """Test Markdown export."""
    test_file = Path(__file__).parent / "test_clippings.txt"
    highlights = parse_clippings(test_file)
    output_file = Path(__file__).parent / "test_output.md"
    
    # Export to Markdown
    from kindle_highlights import export_to_markdown
    export_to_markdown(highlights, output_file)
    
    # Verify output file exists and contains expected content
    assert output_file.exists()
    content = output_file.read_text()
    assert "# The Pragmatic Programmer (Andrew Hunt; David Thomas)" in content
    assert "This is a highlight from the book." in content
    assert "This is a note about the highlight." in content
    assert "# Atomic Habits (James Clear)" in content
    
    # Cleanup
    output_file.unlink()