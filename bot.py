from telegram import Update
from config import Config
from logger import init_logger
from telegram.ext import Application, CommandHandler
from telegram.ext import MessageHandler, filters

logger = init_logger("bot")

BOT_TOKEN = Config.BOT_TOKEN
app = Application.builder().token(BOT_TOKEN).build()

def log_messages(update: Update):
    message = update.message.text
    chat_id = update.message.chat_id
    logger.info(f"Received message: {message} from chat_id: {chat_id}")

async def handle_message(update: Update, context):
    log_messages(update)
    # await update.message.reply_text("Сообщение получено!")

async def start(update: Update, context):
    log_messages(update)
    chat_id = update.message.chat_id
    await update.message.reply_text(f"Привет! Ты авторизован, {chat_id}!")

async def get_chat_id(update: Update, context):
    log_messages(update)
    chat_id = update.message.chat_id
    await update.message.reply_text(f"Ваш chat ID: {chat_id}")

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
app.add_handler(CommandHandler("chatid", get_chat_id))
app.add_handler(MessageHandler(filters.ALL, handle_message))
