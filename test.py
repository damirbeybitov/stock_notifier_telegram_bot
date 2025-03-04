import os
import logging, ngrok
import threading
from fastapi import FastAPI, Request
from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from http.server import HTTPServer, BaseHTTPRequestHandler

import uvicorn

from config import Config

TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = bytes("Hello", "utf-8")
        self.protocol_version = "HTTP/1.1"
        self.send_response(200)
        self.send_header("Content-Length", len(body))
        self.end_headers()
        self.wfile.write(body)

app = FastAPI()
bot = Bot(token=TOKEN)
app_telegram = Application.builder().token(TOKEN).build()

logging.basicConfig(level=logging.INFO)

# Create the server and attach ngrok
# server = HTTPServer(("localhost", 0), HelloHandler)


async def start(update: Update, context):
    await update.message.reply_text("Привет! Я работаю через FastAPI.")


async def echo(update: Update, context):
    await update.message.reply_text(update.message.text)


app_telegram.add_handler(CommandHandler("start", start))
app_telegram.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))


@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    update = Update.de_json(data, bot)
    await app_telegram.process_update(update)
    return {"status": "ok"}


@app.get("/")
async def home():
    return {"message": "Bot webhook is running"}

def run_ngrok():
    # Set up ngrok to forward HTTP traffic to your local server
    public_url = ngrok.connect(8000)
    logging.info(f"Ngrok public URL: {public_url}")
    # Set the Telegram webhook to ngrok URL
    # bot.set_webhook(f"{public_url}/webhook")

def run_server():
    # Start FastAPI app with Uvicorn
    config = uvicorn.Config(app, host="127.0.0.1", port=8000)
    server = uvicorn.Server(config)
    server.run()

# if __name__ == "__main__":
#     # Run ngrok and FastAPI in separate threads
#     threading.Thread(target=run_ngrok).start()
#     threading.Thread(target=run_server).start()

run_server()
