import os
import requests

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_message(text):

    # Telegram limit ≈ 4096
    if len(text) > 3900:
        text = text[:3900] + "\n\n... (truncated)"

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": text
    }

    r = requests.post(url, data=payload)

    print(r.text)
