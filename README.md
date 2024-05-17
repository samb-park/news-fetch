# News API

This project is a simple news API that fetches news articles based on keywords and provides a summary of news articles given their URL. The project uses Flask for the web framework, `feedparser` for parsing RSS feeds, `newspaper3k` for extracting article content, and `transformers` for summarizing the text.

## Features

- Fetch news articles based on a keyword from Google News RSS feed.
- Fetch top news articles from Google News RSS feed.
- Summarize the content of a news article given its URL.

## Endpoints

### POST /summarize

Summarizes the content of a news article.

**Request:**
```json
{
  "url": "https://example.com/news-article"
}