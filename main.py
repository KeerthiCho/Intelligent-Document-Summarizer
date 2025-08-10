import argparse
from src.summarizer.utils import load_text_from_file, load_text_from_url
from src.summarizer.summarize import Summarizer

def main():
    parser = argparse.ArgumentParser(description="Intelligent Document Summarizer")
    parser.add_argument("source_type", choices=["file", "url"], help="Source of the text")
    parser.add_argument("source_path", help="Path to file or URL")
    parser.add_argument("--length", choices=["short", "medium", "long"], default="medium", help="Summary length")
    args = parser.parse_args()

    if args.source_type == "file":
        text = load_text_from_file(args.source_path)
    else:
        text = load_text_from_url(args.source_path)

    summarizer = Summarizer()
    summary = summarizer.summarize(text, length=args.length)

    print("\n=== SUMMARY ===")
    print(summary)

if __name__ == "__main__":
    main()
