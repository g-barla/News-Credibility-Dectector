# src/loaders.py
import newspaper
import tldextract

def load_from_url(url: str):
    """
    Fetch and parse a news article. Returns (title, text).
    """
    article = newspaper.Article(url)
    article.download()
    article.parse()
    title = article.title or ""
    text = article.text or ""
    return title, text