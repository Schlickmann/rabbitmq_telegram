# 🐰📨 RabbitMQ Telegram Notifier

<div align="center">

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![RabbitMQ](https://img.shields.io/badge/RabbitMQ-FF6600?style=flat&logo=rabbitmq&logoColor=white)
![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=flat&logo=telegram&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green.svg)

**A powerful message broker system that forwards RabbitMQ messages to Telegram**

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Configuration](#-configuration)

</div>

---

## 📋 Overview

This project implements a message queue system using **RabbitMQ** that automatically forwards messages to a **Telegram** group or chat. It consists of a publisher that sends messages to a RabbitMQ queue, and a consumer that listens for messages and delivers them to Telegram using the Bot API.

Perfect for:
- 🔔 Real-time notifications
- 📊 System alerts and monitoring
- 🤖 Automated messaging workflows
- 🚀 Decoupled microservices communication

---

## ✨ Features

- ✅ **Asynchronous Message Processing**: Leverage RabbitMQ for reliable message queuing
- ✅ **Telegram Integration**: Seamless delivery to Telegram groups or private chats
- ✅ **Persistent Messages**: Messages survive broker restarts
- ✅ **Environment-based Configuration**: Secure credential management with `.env`
- ✅ **Simple Architecture**: Easy to understand and extend
- ✅ **Error Handling**: Robust message delivery system

---

## 🏗️ Architecture

```
┌─────────────┐        ┌──────────────┐        ┌─────────────┐        ┌──────────────┐
│  Publisher  │───────▶│   RabbitMQ   │───────▶│  Consumer   │───────▶│   Telegram   │
│   (Sender)  │        │    Queue     │        │  (Listener) │        │   Bot API    │
└─────────────┘        └──────────────┘        └─────────────┘        └──────────────┘
      ▲                                               │
      │                                               ▼
   Your App                                    Your Telegram Group
```

---

## 📦 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8+**
- **RabbitMQ Server** (local or remote instance)
- **Telegram Bot Token** (from [@BotFather](https://t.me/botfather))
- **pip** (Python package manager)

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Schlickmann/rabbitmq_telegram.git
cd rabbitmq_telegram
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv

# Activate on macOS/Linux
source .venv/bin/activate

# Activate on Windows
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the root directory:

```bash
cp .env.example .env
```

Edit `.env` with your configuration (see [Configuration](#-configuration) section below).

---

## ⚙️ Configuration

Create a `.env` file with the following variables:

```env
# RabbitMQ Configuration
RABBITMQ_HOST=localhost
RABBITMQ_PORT=5672
RABBITMQ_USERNAME=guest
RABBITMQ_PASSWORD=guest
RABBITMQ_QUEUE=telegram_queue
RABBITMQ_EXCHANGE=telegram_exchange
RABBITMQ_ROUTING_KEY=telegram

# Telegram Configuration
TELEGRAM_TOKEN=your_bot_token_here
TELEGRAM_GROUP_ID=your_chat_id_here
```

### 🔑 Getting Telegram Credentials

1. **Bot Token**: 
   - Message [@BotFather](https://t.me/botfather) on Telegram
   - Send `/newbot` and follow the instructions
   - Copy your bot token

2. **Chat/Group ID**:
   - Add your bot to the desired group
   - Visit: `https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates`
   - Look for `"chat":{"id":` in the response
   - Use that ID as `TELEGRAM_GROUP_ID`

---

## 💻 Usage

### Starting RabbitMQ Server

If running RabbitMQ locally:

```bash
# macOS (with Homebrew)
brew services start rabbitmq

# Linux
sudo systemctl start rabbitmq-server

# Docker
docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
```

### Running the Consumer

The consumer listens for messages and forwards them to Telegram:

```bash
python run.py
```

You should see:
```
Waiting for messages. Connected to RabbitMQ
```

### Publishing Messages

In a separate terminal, you can publish messages in two ways:

#### Option 1: Using the Publisher Module

```python
# publisher.py
from publisher import RabbitMQPublisher

rabbitmq_publisher = RabbitMQPublisher()
rabbitmq_publisher.publish({
    "message": "Hello! This is your notification 🚀"
})
```

Run:
```bash
python publisher.py
```

#### Option 2: Direct Telegram Sender (Testing)

```bash
python sender.py
```

---

## 📁 Project Structure

```
rabbitmq_telegram/
│
├── src/
│   ├── __init__.py
│   ├── drivers/
│   │   ├── __init__.py
│   │   └── telegram_sender.py      # Telegram API integration
│   │
│   └── main/
│       ├── __init__.py
│       └── rabbitmq_config/
│           ├── __init__.py
│           ├── consumer.py          # RabbitMQ consumer
│           └── callback.py          # Message processing callback
│
├── publisher.py                     # Message publisher
├── sender.py                        # Direct Telegram sender (testing)
├── run.py                          # Consumer entry point
├── requirements.txt                # Python dependencies
├── .env.example                    # Environment template
├── .env                           # Your local config (not in git)
└── .gitignore                     # Git ignore rules
```

---

## 🔧 Development

### Message Format

Messages published to RabbitMQ should follow this JSON structure:

```json
{
  "message": "Your notification text here"
}
```

### Extending Functionality

To add more features, you can:

1. **Add message types**: Extend the callback to handle different message formats
2. **Add retry logic**: Implement exponential backoff for failed deliveries
3. **Add logging**: Use Python's `logging` module for better observability
4. **Add multiple consumers**: Scale horizontally for high-volume scenarios

---

## 🐛 Troubleshooting

### Consumer Not Receiving Messages

- Verify RabbitMQ is running: `sudo systemctl status rabbitmq-server`
- Check queue exists: Visit `http://localhost:15672` (default credentials: `guest`/`guest`)
- Ensure routing key matches between publisher and consumer

### Telegram Messages Not Sending

- Verify bot token is correct
- Ensure bot is added to the target group
- Check chat ID is correct (should be negative for groups)
- Verify network connectivity to Telegram API

### Connection Refused Errors

- Check RabbitMQ host and port in `.env`
- Ensure RabbitMQ service is running
- Verify credentials are correct

---

## 📚 Resources

- [RabbitMQ Documentation](https://www.rabbitmq.com/documentation.html)
- [Telegram Bot API](https://core.telegram.org/bots/api)
- [Pika Documentation](https://pika.readthedocs.io/)
- [Rocketseat](https://www.rocketseat.com.br/)

---

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Julian Schlickmann**

- GitHub: [@Schlickmann](https://github.com/Schlickmann)
- Email: juliani.schlickmann@gmail.com

---

<div align="center">

**⭐ If you found this project helpful, please give it a star!**

Made with ❤️ and ☕ by Julian Schlickmann

</div>

