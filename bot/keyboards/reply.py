from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


reply_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Марвел',)],
        [
            KeyboardButton(text='Заклятие'),
            KeyboardButton(text='Чужой')
        ],
        [KeyboardButton(text='Звёздные войны')],
        [KeyboardButton(text='Властелин колец')]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder='Выберете хронологию!',
)