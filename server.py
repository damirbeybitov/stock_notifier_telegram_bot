from fastapi import FastAPI
import asyncio

import uvicorn
from bot import send_message, start_bot
from config import Config
from logger import init_logger

logger = init_logger("server")

app = FastAPI()

@app.get("/")
async def ping():
    return {"status": "ok", "message": "pong"}

@app.post("/notify/")
async def notify_user(chat_id: int, message: str):
    """Принимает chat_id и message, отправляет сообщение пользователю через бота."""
    asyncio.create_task(send_message(chat_id, message))  # Отправляем сообщение асинхронно
    return {"status": "ok", "message": "Notification sent"}

# async def start_server():
#     """Функция-заглушка для main.py, чтобы сервер работал в asyncio.gather()"""
#     import uvicorn

#     config = Config.FASTAPI_HOST, Config.FASTAPI_PORT
#     try:
#         config = uvicorn.Config(app, host="127.0.0.1", port=8000)
#         server = uvicorn.Server(config)
#         await server.serve()
#     except Exception as e:
#         logger.error(e)

if __name__ == "__main__":
    start_bot()
    uvicorn.run(app, host="127.0.0.1", port=8000)