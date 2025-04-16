import asyncio
import nest_asyncio
from telegram import Update
from config import Config
from logger import init_logger
from telegram.ext import Application, CommandHandler
from telegram.ext import MessageHandler, filters

nest_asyncio.apply()

logger = init_logger("bot")

BOT_TOKEN = Config.BOT_TOKEN
# request = HTTPXRequest(connect_timeout=15.0, read_timeout=15.0)
# .request(request)
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
    await update.message.reply_text(f"Привет! Ваш chat ID:")
    await update.message.reply_text(chat_id)

async def main():
    print("Starting bot...")
    logger.info("Starting bot...")

    await app.bot.delete_webhook(drop_pending_updates=True)

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.ALL, handle_message))

    # запуск синхронный, без await
    app.run_polling()

if __name__ == "__main__":
    import asyncio
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped manually")
        logger.info("Bot stopped manually")
    except Exception as e:
        logger.error(f"Error: {e}")