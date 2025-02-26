import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command
from config import Config

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("bot")

# Чтение токена из конфигурационного файла
BOT_TOKEN = Config.BOT_TOKEN

# Создаем экземпляры бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command('start'))
async def start(message: Message):
    """Обработчик команды /start для аутентификации пользователя"""
    chat_id = message.chat.id
    # Здесь может быть логика для аутентификации пользователя
    await message.answer(f"Привет! Ты авторизован, {chat_id}!")

async def send_message(chat_id: int, text: str):
    """Функция для отправки уведомлений"""
    await bot.send_message(chat_id=chat_id, text=text)

async def start_bot():
    try:
        await dp.start_polling(bot)
    except Exception as e:
        logger.error(e)

if __name__ == "__main__":
    asyncio.run(start_bot())