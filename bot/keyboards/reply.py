from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


reply_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Марвел')],
        [KeyboardButton(text='Заклятие'), KeyboardButton(text='Властелин колец')],
        [KeyboardButton(text='Звёздные войны')]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder='Выберете хронологию!',
)