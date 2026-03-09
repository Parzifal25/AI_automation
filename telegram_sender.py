import requests
import os

def send_message(text):

    url = f"https://api.telegram.org/bot{os.getenv('TELEGRAM_BOT_TOKEN')}/sendMessage"

    payload = {
        "chat_id": os.getenv("TELEGRAM_CHAT_ID"),
        "text": text
    }

    r = requests.post(url, data=payload)

    print(r.text)
