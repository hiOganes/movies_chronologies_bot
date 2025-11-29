from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


inline_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Выбрать хронологию', 
                callback_data='start'
            )
        ]
    ]
)
