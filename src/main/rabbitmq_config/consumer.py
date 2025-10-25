import pika
import os
from src.main.rabbitmq_config.callback import rabbitmq_callback


class RabbitMQConsumer:
    def __init__(self) -> None:
        self.__host = os.getenv("RABBITMQ_HOST")
        self.__port = os.getenv("RABBITMQ_PORT")
        self.__username = os.getenv("RABBITMQ_USERNAME")
        self.__password = os.getenv("RABBITMQ_PASSWORD")
        self.__queue = os.getenv("RABBITMQ_QUEUE")
        self.__channel = self.create_channel()

    def create_channel(self):
        connection_parameters = pika.ConnectionParameters(
            host=self.__host,
            port=self.__port,
            credentials=pika.PlainCredentials(self.__username, self.__password),
        )
        channel = pika.BlockingConnection(connection_parameters).channel()
        channel.queue_declare(queue=self.__queue, durable=True)
        channel.basic_consume(queue=self.__queue, auto_ack=True, on_message_callback=rabbitmq_callback)
        return channel
    
    def consume(self) -> None:
        print('Waiting for messages. Connected to RabbitMQ')
        self.__channel.start_consuming()