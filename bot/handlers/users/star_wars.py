from aiogram import Router, F
from aiogram.types import Message

from bot.utils.cache_movies import get_cached_movies, set_cache_movies
from bot.keyboards.inline import inline_menu


star_wars_router = Router()

all_movies = {
    1: "Эпизод I — Скрытая угроза",
    2: "Эпизод II — Атака клонов",
    3: "Войны клонов (сериал)",
    4: "Эпизод III — Месть ситхов",
    5: "Бракованная партия (сериал)",
    6: "Хан Соло: Звёздные войны. Истории",
    7: "Андор (сериал)",
    8: "Оби-Ван Кеноби (сериал)",
    9: "Повстанцы (сериал)",
    10: "Изгой-один: Звёздные войны. Истории",
    11: "Эпизод IV — Новая надежда",
    12: "Эпизод V — Империя наносит ответный удар",
    13: "Эпизод VI — Возвращение джедая",
    14: "Мандалорец (сериал)",
    15: "Книга Бобы Фетта (сериал)",
    16: "Асока (сериал)",
    17: "Сопротивление (сериал)",
    18: "Эпизод VII — Пробуждение Силы",
    19: "Эпизод VIII — Последние джедаи",
    20: "Эпизод IX — Скайуокер. Восход",
    21: "Видения (антология)",
    22: "Скелетная команда (сериал)",
    23: "Аколит (сериал)",
}

@star_wars_router.message(F.text == 'Звёздные войны')
async def star_wars_chronology(message: Message):
    movies = await get_cached_movies('star_wars')

    if movies:
        await message.answer(movies, reply_markup=inline_menu)
    else:
        chronology = []
        for movie in all_movies.items():
            chronology.append(f'{movie[0]} -- {movie[1]}')
        
        result = 'Хронология Звёздных войн: \n\n' + '\n'.join(chronology)
        await message.answer(result, reply_markup=inline_menu)
        await set_cache_movies('star_wars', result)
