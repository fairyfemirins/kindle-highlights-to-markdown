import click
from .parser import parse_clippings
from .exporter import export_to_markdown

@click.command()
@click.option("--input", type=click.Path(exists=True), required=True, help="Path to My Clippings.txt")
@click.option("--output", type=click.Path(), required=True, help="Output markdown file")
@click.option("--format", type=click.Choice(["obsidian", "notion", "logseq"]), default="obsidian", help="Output format")
def cli(input, output, format):
    books = parse_clippings(input)
    template_path = f"kindle2md/templates/{format}.md"
    export_to_markdown(books, template_path, output)
    click.echo(f"Exported {len(books)} books to {output}")

if __name__ == "__main__":
    cli()