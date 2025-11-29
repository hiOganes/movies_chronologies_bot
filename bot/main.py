import os
import asyncio

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

from bot.handlers.users.start import start_router
from bot.handlers.users.marvel import marvel_router


load_dotenv()

async def main():
    bot = Bot(os.getenv('TOKEN'))
    dp = Dispatcher()   
    dp.include_routers(start_router, marvel_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())