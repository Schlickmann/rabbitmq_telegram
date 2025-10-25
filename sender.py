import requests
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN", "")
CHAT_ID = os.getenv("TELEGRAM_GROUP_ID", "")

def send_telegram_message(token: str, chat_id: str, message: str) -> None:
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }
    response = requests.post(url, data=payload)
    print(response.json())

send_telegram_message(TOKEN, CHAT_ID, "Sending message to Telegram group using API")