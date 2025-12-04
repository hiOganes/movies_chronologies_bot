import os
import asyncio

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

from bot.handlers.users.start import start_router
from bot.handlers.users.marvel import marvel_router
from bot.handlers.users.conjuring import conjuring_router
from bot.handlers.users.alien import alien_router
from bot.callbacks.menu import callback_menu_router
from bot.handlers.users.star_wars import star_wars_router
from bot.handlers.users.lord_of_the_rings import lord_of_the_rings_router
from bot.middlewares.delete_user_message import DeleteUserMessageMiddleware


load_dotenv()

async def main():
    bot = Bot(os.getenv('TOKEN'))
    dp = Dispatcher()   
    dp.include_routers(
        start_router, 
        marvel_router, 
        callback_menu_router, 
        conjuring_router, 
        star_wars_router, 
        lord_of_the_rings_router,
        alien_router
    )
    # dp.message.middleware(DeleteUserMessageMiddleware())
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
    