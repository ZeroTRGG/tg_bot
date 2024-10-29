import logging
import asyncio
import sys

from aiogram import Bot, Dispatcher

from config import TOKEN
from handler import router
from temp import add_to_startup

bot = Bot(token=TOKEN)

dp = Dispatcher(bot=bot)

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())