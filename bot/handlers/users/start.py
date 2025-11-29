from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart


start_router = Router()

@start_router.message(CommandStart())
async def start(message: Message):
    await message.reply(f'Привет, {message.from_user.first_name}!')