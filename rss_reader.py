import feedparser
from datetime import datetime

def extract_source_from_title(title):
    """
    Extract the source from the news title if available.
    """
    if ' - ' in title:
        return title.split(' - ')[-1]
    return "Unknown"

def get_news(keyword):
    """
    Fetch news articles based on a keyword from Google News RSS feed.
    """
    base_url = "https://news.google.com/rss/search"
    query = f"?q={keyword}"
    rss_url = base_url + query
    
    feed = feedparser.parse(rss_url)

    news_items = []
    for entry in feed.entries:
        # Convert the published date to "17 May 2024" format
        published_date = datetime.strptime(entry.published, '%a, %d %b %Y %H:%M:%S %Z')
        formatted_date = published_date.strftime('%d %b %Y')
        
        source = entry.source.title if 'source' in entry else extract_source_from_title(entry.title)
        
        news_items.append({
            "title": entry.title,
            "link": entry.link,
            "published": formatted_date,
            "source": source
        })
    
    return news_items

def get_top_news():
    """
    Fetch top news articles from Google News RSS feed.
    """
    rss_url = "https://news.google.com/rss?hl=en-US&gl=US&ceid=US:en"
    
    feed = feedparser.parse(rss_url)

    news_items = []
    for entry in feed.entries:
        # Convert the published date to "17 May 2024" format
        published_date = datetime.strptime(entry.published, '%a, %d %b %Y %H:%M:%S %Z')
        formatted_date = published_date.strftime('%d %b %Y')
        
        source = entry.source.title if 'source' in entry else extract_source_from_title(entry.title)
        
        news_items.append({
            "title": entry.title,
            "link": entry.link,
            "published": formatted_date,
            "source": source
        })
    
    return news_items