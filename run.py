import asyncio
import logging
import os
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher

from app.db.engine import create_db, drop_db, session_maker
from app.handiers.user import router
from app.middlewares.db import DataBaseSession

load_dotenv()
bot = Bot(token=os.environ.get("TOKEN"))
dp = Dispatcher()


async def on_startup(bot: Bot, run_param: bool = False):
    run_param = False
    if run_param:
        await drop_db()

    await create_db()


async def on_shutdown(bot: Bot):
    print("бот лег")


async def mein():
    dp.include_router(router)

    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    dp.update.middleware(DataBaseSession(session_pool=session_maker))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(mein())
    except KeyboardInterrupt:
        print("Exit")
