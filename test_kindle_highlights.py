import pytest
from kindle_highlights import KindleHighlight, parse_clippings, export_to_markdown
from pathlib import Path
import tempfile


def test_kindle_highlight_parsing():
    """Test KindleHighlight class."""
    highlight = KindleHighlight(
        book="Test Book",
        author="Test Author",
        text="This is a test highlight. #tag1 #tag2",
        location="123-124",
        date="Friday, May 15, 2026, 2:49 PM",
    )
    assert highlight.book == "Test Book"
    assert highlight.tags == ["tag1", "tag2"]
    assert "> This is a test highlight. #tag1 #tag2" in highlight.to_markdown()


def test_parse_clippings():
    """Test parsing of My Clippings.txt."""
    sample_clippings = """Test Book (Test Author)
- Your Highlight on Location 123-124 | Added on Friday, May 15, 2026, 2:49 PM

This is a test highlight.
======
"""
    with tempfile.NamedTemporaryFile(mode="w", delete=False) as f:
        f.write(sample_clippings)
        f.flush()
        highlights = parse_clippings(f.name)

    assert "Test Book" in highlights
    assert len(highlights["Test Book"]) == 1
    assert highlights["Test Book"][0].text == "This is a test highlight."


def test_export_to_markdown():
    """Test Markdown export."""
    highlights = {
        "Test Book": [
            KindleHighlight(
                book="Test Book",
                author="Test Author",
                text="This is a test highlight.",
                location="123-124",
                date="Friday, May 15, 2026, 2:49 PM",
            )
        ]
    }
    with tempfile.TemporaryDirectory() as tmpdir:
        export_to_markdown(highlights, tmpdir)
        output_file = Path(tmpdir) / "Test Book.md"
        assert output_file.exists()
        content = output_file.read_text()
        assert "# Test Book" in content
        assert "This is a test highlight." in content