import json
from src.drivers.telegram_sender import send_telegram_message

def rabbitmq_callback(ch, method, properties, body):
  message = body.decode("utf-8")
  message_data = json.loads(message)
  telegram_message = message_data['message']
  send_telegram_message(telegram_message)

