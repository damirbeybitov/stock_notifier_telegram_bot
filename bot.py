import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command
from config import Config
from logger import init_logger

logger = init_logger("bot")

BOT_TOKEN = Config.BOT_TOKEN
app = Application.builder().token(BOT_TOKEN).build()

async def start(update: Update, context):
    chat_id = update.message.chat_id
    await update.message.reply_text(f"Привет! Ты авторизован, {chat_id}!")

async def send_message(chat_id: int, message: str):
    await app.bot.send_message(chat_id=chat_id, text=message)

async def process_update(update: dict):
    try:
        tg_update = Update.de_json(update, app.bot)
        await app.process_update(tg_update)
    except Exception as e:
        logger.error(f"Ошибка при обработке обновления: {e}")

async def set_webhook(webhook_url: str):
    """Устанавливает вебхук"""
    await app.bot.set_webhook(url=webhook_url)

# Initialize the application
async def initialize_app():
    await app.initialize()

app.add_handler(CommandHandler("start", start))
