import os
import requests
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def split_message(text, limit=4000):
    return [text[i:i+limit] for i in range(0, len(text), limit)]

def send_telegram_message(message):

    if not BOT_TOKEN or not CHAT_ID:
        print("ERROR: Telegram token or chat id missing")
        return

    messages = split_message(message)

    for msg in messages:

        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

        payload = {
            "chat_id": CHAT_ID,
            "text": msg
        }

        response = requests.post(url, json=payload)

        print("Telegram response:", response.text)