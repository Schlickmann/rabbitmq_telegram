from dotenv import load_dotenv
from src.main.rabbitmq_config.consumer import RabbitMQConsumer

load_dotenv()

if __name__ == "__main__":
    rabbitmq_consumer = RabbitMQConsumer()
    rabbitmq_consumer.consume()