from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='/test1'), KeyboardButton(text='/test2')],
        [KeyboardButton(text='/marvel')],
        [KeyboardButton(text='/test3'), KeyboardButton(text='/test4')]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder='Выберете хронологию!',
)