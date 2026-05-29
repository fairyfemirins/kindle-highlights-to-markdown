import pytest
from kindle2md.exporter import export_to_markdown
from kindle2md.parser import Book, Highlight

def test_export_to_markdown(tmp_path):
    books = [
        Book(
            title="Test Book",
            author="Test Author",
            highlights=[Highlight(text="Test highlight", page="42", location="123")],
        )
    ]
    template_path = "kindle2md/templates/obsidian.md"
    output_path = tmp_path / "output.md"
    export_to_markdown(books, template_path, str(output_path))
    assert "# Test Book" in output_path.read_text()
    assert "Test highlight" in output_path.read_text()