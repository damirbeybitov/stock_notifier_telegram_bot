from telegram import Update
from telegram.ext import Application, CommandHandler
from config import Config

# Чтение токена из переменных окружения или конфигурационного файла
BOT_TOKEN = Config.BOT_TOKEN

# Создаем экземпляр бота
app = Application.builder().token(BOT_TOKEN).build()

async def start(update: Update, context):
    """Обработчик команды /start для аутентификации пользователя"""
    chat_id = update.message.chat_id
    # Здесь может быть логика для аутентификации пользователя, например, запись в базу данных
    await update.message.reply_text(f"Привет! Ты авторизован, {chat_id}!")

async def send_message(chat_id: int, message: str):
    """Функция для отправки уведомлений"""
    await app.bot.send_message(chat_id=chat_id, text=message)

# Регистрация обработчиков команд
app.add_handler(CommandHandler("start", start))

def start_bot():
    """Запуск бота"""
    app.run_polling()
