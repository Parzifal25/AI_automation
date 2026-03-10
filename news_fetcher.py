import feedparser


def get_top_news(feed_url, limit=5):
    feed = feedparser.parse(feed_url)

    news = []

    for entry in feed.entries[:limit]:
        news.append(f"• {entry.title}")

    return "\n".join(news)


def fetch_news():

    tech_news = get_top_news(
        "https://www.theverge.com/rss/index.xml"
    )

    geopolitics_news = get_top_news(
        "https://feeds.bbci.co.uk/news/world/rss.xml"
    )

    indian_market_news = get_top_news(
        "https://www.moneycontrol.com/rss/business.xml"
    )

    movie_news = get_top_news(
        "https://variety.com/feed/"
    )

    news_report = f"""
📰 NEWS BRIEF

💻 Tech (Top 5)
{tech_news}

🌍 Geopolitics (Top 5)
{geopolitics_news}

📈 Indian Markets (Top 5)
{indian_market_news}

🎬 Movies (Top 5)
{movie_news}
"""

    return news_report