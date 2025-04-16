import os
from dotenv import load_dotenv

load_dotenv()
from dotenv import load_dotenv

load_dotenv('.env')

class Config:
    """Класс для хранения конфигураций проекта."""

    # Токен для Telegram бота
    BOT_TOKEN = os.getenv("BOT_TOKEN")
