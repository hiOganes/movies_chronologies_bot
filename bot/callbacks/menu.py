from aiogram import F, Router
from aiogram.types import CallbackQuery

from bot.keyboards.reply import reply_menu
from bot.handlers.users.marvel import marvel_router


callback_menu_router = Router()

@callback_menu_router.callback_query(F.data == 'menu')
async def menu(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer('Выберете хронологию', 
                                  reply_markup=reply_menu)
    await callback.answer()
    