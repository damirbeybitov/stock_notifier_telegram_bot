import os

class Config:
    """Класс для хранения конфигураций проекта."""

    # Токен для Telegram бота
    BOT_TOKEN = os.getenv("BOT_TOKEN", "your_default_bot_token_here")

    # Параметры для FastAPI сервера
    FASTAPI_HOST = os.getenv("FASTAPI_HOST", "0.0.0.0")
    FASTAPI_PORT = int(os.getenv("FASTAPI_PORT", 8000))

# Пример использования
config = Config()
print(config.BOT_TOKEN)