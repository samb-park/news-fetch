from newspaper import Article
from transformers import pipeline

summarizer = pipeline("summarization")

def summarize_text(url):
    """
    Summarize the text content of a news article given its URL.
    """
    article = Article(url)
    article.download()
    article.parse()

    text = article.text

    summary = summarizer(text, max_length=150, min_length=30, do_sample=False)
    summary_text = summary[0]['summary_text']
    
    return summary_text