from fastapi import FastAPI
import asyncio
from bot import send_message
from config import Config  # Функция для отправки сообщений через бота
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/notify/")
async def notify_user(chat_id: int, message: str):
    """Принимает chat_id и message, отправляет сообщение пользователю через бота."""
    asyncio.create_task(send_message(chat_id, message))  # Отправляем сообщение асинхронно
    return {"status": "ok", "message": "Notification sent"}

async def start_server():
    """Функция-заглушка для main.py, чтобы сервер работал в asyncio.gather()"""
    config = Config.FASTAPI_HOST, Config.FASTAPI_PORT
    uvicorn.run(app, host=config[0], port=config[1])
    

# if __name__ == "__main__":
#     config = Config.FASTAPI_HOST, Config.FASTAPI_PORT
#     print(config)
#     uvicorn.run(app, host=config[0], port=config[1])