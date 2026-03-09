from news_fetcher import get_news
from ai_briefing import generate_brief
from telegram_sender import send_message
import datetime

def run():
    news = get_news()
    report = generate_brief(news)
    message = f"📊 AI Command Center {datetime.date.today()}\n\n{report}"
    send_message(message)

if __name__ == "__main__":
    run()
