import asyncio
from bot import start_bot
from server import start_server

async def main():
    # Запускаем сервер FastAPI и бота параллельно
    await asyncio.gather(start_server(), start_bot())

if __name__ == "__main__":
    asyncio.run(main())
