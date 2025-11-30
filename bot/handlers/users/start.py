from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart

from bot.keyboards.reply import reply_menu


start_router = Router()

@start_router.message(CommandStart())
async def start(message: Message):
    await message.reply(
        f'Привет, {message.from_user.first_name}!', reply_markup=reply_menu,
        )
