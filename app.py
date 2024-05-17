from flask import Flask, request, jsonify
from rss_reader import get_news, get_top_news
from summarizer import summarize_text

app = Flask(__name__)

@app.route('/summarize', methods=['POST'])
def summarize():
    """
    Endpoint to summarize the content of a news article given its URL.
    """
    data = request.get_json()
    url = data.get('url')

    if not url:
        return jsonify({"error": "URL is required"}), 400

    summary = summarize_text(url)

    return jsonify({
        "url": url,
        "summary": summary
    })

@app.route('/news', methods=['POST'])
def news():
    """
    Endpoint to get news articles based on a keyword.
    """
    data = request.get_json()
    keyword = data.get('keyword', '')

    if not keyword:
        return jsonify({"error": "Keyword is required"}), 400

    news_items = get_news(keyword)

    return jsonify(news_items)

@app.route('/news_top', methods=['GET'])
def news_top():
    """
    Endpoint to get top news articles.
    """
    news_items = get_top_news()
    return jsonify(news_items)

if __name__ == '__main__':
    app.run(port=5001)