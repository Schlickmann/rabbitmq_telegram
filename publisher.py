import os
from dotenv import load_dotenv
import pika
import json

load_dotenv()

class RabbitMQPublisher:
    def __init__(self) -> None:
        self.__host = os.getenv("RABBITMQ_HOST")
        self.__port = os.getenv("RABBITMQ_PORT")
        self.__username = os.getenv("RABBITMQ_USERNAME")
        self.__password = os.getenv("RABBITMQ_PASSWORD")
        self.__exchange = os.getenv("RABBITMQ_EXCHANGE")
        self.__routing_key = os.getenv("RABBITMQ_ROUTING_KEY")
        self.__channel = self.create_channel()

    def create_channel(self):
        connection_parameters = pika.ConnectionParameters(
            host=self.__host,
            port=self.__port,
            credentials=pika.PlainCredentials(self.__username, self.__password),
        )
        channel = pika.BlockingConnection(connection_parameters).channel()
        return channel
    
    def publish(self, body: dict) -> None:
        self.__channel.basic_publish(
            exchange=self.__exchange, 
            routing_key=self.__routing_key, 
            body=json.dumps(body), 
            properties=pika.BasicProperties(delivery_mode=2) # 2 means persistent
        )
        print(f" [x] Sent {body}")

rabbitmq_publisher = RabbitMQPublisher()
rabbitmq_publisher.publish({
    "message": "Hello, Julian! This is a test message. It should be sent to the Telegram group using RabbitMQ"
})
