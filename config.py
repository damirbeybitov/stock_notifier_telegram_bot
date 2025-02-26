import os
from dotenv import load_dotenv

load_dotenv('.env')

class Config:
    """Класс для хранения конфигураций проекта."""

    # Токен для Telegram бота
    BOT_TOKEN = os.getenv("BOT_TOKEN", "asd")

    # Параметры для FastAPI сервера
    FASTAPI_HOST = os.getenv("FASTAPI_HOST", "127.0.0.1")
    FASTAPI_PORT = int(os.getenv("FASTAPI_PORT", 8000))

config = Config()
print(config.BOT_TOKEN)