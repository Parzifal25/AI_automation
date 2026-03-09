import feedparser

sources = {
    "tech": "https://techcrunch.com/feed/",
    "geopolitics": "http://feeds.reuters.com/reuters/worldNews",
    "stocks": "https://www.moneycontrol.com/rss/business.xml",
    "movies": "https://variety.com/feed/"
}

def get_news():

    news_data = {}

    for category, url in sources.items():
        feed = feedparser.parse(url)

        headlines = []
        for entry in feed.entries[:5]:
            headlines.append(entry.title)

        news_data[category] = headlines

    return news_data