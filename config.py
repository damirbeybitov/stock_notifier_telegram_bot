import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Класс для хранения конфигураций проекта."""

    # Токен для Telegram бота
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    # Токен для ngrok
    NGROK_AUTH_TOKEN = os.getenv("NGROK_AUTH_TOKEN")

    # Параметры для FastAPI сервера
    FASTAPI_HOST = os.getenv("FASTAPI_HOST", "127.0.0.1")
    FASTAPI_PORT = int(os.getenv("FASTAPI_PORT", 8000))
