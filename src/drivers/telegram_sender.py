import requests
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN", "")
CHAT_ID = os.getenv("TELEGRAM_GROUP_ID", "")

def send_telegram_message(message: str) -> None:
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    requests.post(url, data=payload)
