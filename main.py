import schedule
import time
import datetime

from news_fetcher import get_news
from ai_briefing import generate_brief
from telegram_sender import send_message


def daily_run():

    print("Running AI OS...")

    news = get_news()

    report = generate_brief(news)

    message = f"📊 AI Command Center {datetime.date.today()}\n\n{report}"

    send_message(message)

    print("Report sent")


schedule.every().minute.do(daily_run)

while True:

    schedule.run_pending()
    time.sleep(60)
