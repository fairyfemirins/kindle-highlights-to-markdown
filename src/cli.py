# cli.py
import argparse
from .parser import parse_clippings
from .formatter import to_markdown


def main():
    parser = argparse.ArgumentParser(description="Convert Kindle highlights to Markdown.")
    parser.add_argument("file_path", help="Path to My Clippings.txt")
    parser.add_argument("--output", "-o", default="output", help="Output directory for Markdown files")
    args = parser.parse_args()

    highlights = parse_clippings(args.file_path)
    to_markdown(highlights, args.output)
    print(f"Converted {len(highlights)} highlights to Markdown in '{args.output}/'")


if __name__ == "__main__":
    main()