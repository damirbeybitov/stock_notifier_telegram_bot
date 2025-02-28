from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
import asyncio
import uvicorn
import subprocess
import requests
import ngrok
from bot import initialize_app, send_message, process_update, set_webhook
from config import Config
from logger import init_logger

logger = init_logger("server")

# async def get_ngrok_url():
#     """Запускает ngrok и получает URL для вебхука"""
#     subprocess.Popen(["ngrok", "http", str(Config.FASTAPI_PORT)], stdout=subprocess.DEVNULL)
#     await asyncio.sleep(2)  # Даем ngrok время запуститься
#     response = requests.get("http://localhost:4040/api/tunnels")
#     tunnels = response.json().get("tunnels", [])
#     for tunnel in tunnels:
#         if tunnel.get("proto") == "https":
#             return tunnel.get("public_url")
#     return None

async def get_ngrok_url():
    """Запускает ngrok и получает URL для вебхука"""
    ngrok.set_auth_token(Config.NGROK_AUTH_TOKEN)
    listener = await ngrok.connect(Config.FASTAPI_PORT, "http")
    # logger.info(f'Ngrok: {listener}')
    # logger.info(f'Ngrok id: {listener.id()}')
    # logger.info(f'Ngrok labels: {listener.labels()}')
    # logger.info(f'Ngrok metadata: {listener.metadata()}')
    # logger.info(f'Ngrok url: {listener.url()}')
    return listener.url()

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Запускается при старте сервера, устанавливает вебхук"""
    global WEBHOOK_URL
    WEBHOOK_URL = await get_ngrok_url()
    if WEBHOOK_URL:
        logger.info(f"Webhook URL: {WEBHOOK_URL}")
        await set_webhook(WEBHOOK_URL + "/webhook")
        await initialize_app()
    else:
        print("Ошибка: Не удалось получить Webhook URL")
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/ping")
async def ping():
    return {"status": "ok", "message": "pong"}

@app.post("/notify")
async def notify_user(chat_id: int, message: str):
    asyncio.create_task(send_message(chat_id, message))
    return {"status": "ok", "message": "Notification sent"}

@app.post("/webhook")
async def telegram_webhook(request: Request):
    try:
        update = await request.json()
        asyncio.create_task(process_update(update))
        return {"status": "ok"}
    except Exception as e:
        logger.error("Ошибка при обработке вебхука")
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    try:
        uvicorn.run(app, host=Config.FASTAPI_HOST, port=Config.FASTAPI_PORT, log_config=None, log_level="info")
    except Exception as e:
        logger.error("Ошибка при запуске сервера")