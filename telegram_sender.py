import os
import requests

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

MAX_LEN = 4000


def send_message(text):

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    # split message into chunks
    parts = [text[i:i+MAX_LEN] for i in range(0, len(text), MAX_LEN)]

    for part in parts:

        payload = {
            "chat_id": CHAT_ID,
            "text": part
        }

        r = requests.post(url, data=payload)

        print(r.text)
