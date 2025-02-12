from fastapi import FastAPI
import asyncio
from bot import send_message
from config import Config  # Функция для отправки сообщений через бота

app = FastAPI()

@app.post("/notify/")
async def notify_user(chat_id: int, message: str):
    """Принимает chat_id и message, отправляет сообщение пользователю через бота."""
    asyncio.create_task(send_message(chat_id, message))  # Отправляем сообщение асинхронно
    return {"status": "ok", "message": "Notification sent"}

async def start_server():
    """Функция-заглушка для main.py, чтобы сервер работал в asyncio.gather()"""
    import uvicorn
    config = Config.FASTAPI_HOST, Config.FASTAPI_PORT
    await uvicorn.run(app, host=config[0], port=config[1])  
