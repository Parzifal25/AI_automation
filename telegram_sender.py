import os
import requests

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

<<<<<<< HEAD
def split_message(text, limit=4000):
    return [text[i:i+limit] for i in range(0, len(text), limit)]
=======
MAX_LEN = 4000


def send_message(text):
>>>>>>> fba49e2ed82e3084ce601d978ebec102dcec0d6f

def send_telegram_message(message):

<<<<<<< HEAD
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
=======
    # split message into chunks
    parts = [text[i:i+MAX_LEN] for i in range(0, len(text), MAX_LEN)]

    for part in parts:

        payload = {
            "chat_id": CHAT_ID,
            "text": part
        }

        r = requests.post(url, data=payload)

        print(r.text)
>>>>>>> fba49e2ed82e3084ce601d978ebec102dcec0d6f
