import requests
from newspaper import Article
import os

def load_text_from_file(file_path):
    """Load text content from a local file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def load_text_from_url(url):
    """Extract main article text from a URL."""
    article = Article(url)
    article.download()
    article.parse()
    return article.text
