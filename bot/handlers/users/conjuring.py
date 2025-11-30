from aiogram import Router, F
from aiogram.types import Message

from bot.utils.cache_movies import get_cached_movies, set_cache_movies
from bot.keyboards.inline import inline_menu


conjuring_router = Router()

all_movies = {
    1: 'Проклятие монахини', 
    2: 'Проклятие Аннабель: Зарождение зла',
    3: 'Проклятие монахини 2',
    4: 'Проклятие Аннабель',
    5: 'Заклятие',
    6: 'Проклятие Аннабель 3',
    7: 'Проклятие плачущей',
    8: 'Заклятие 2',
    9: 'Заклятие 3',
    10: 'Заклятие 4',
}

@conjuring_router.message(F.text == 'Заклятие')
async def get_conjuring_chronology(message: Message):
    movies = await get_cached_movies('conjuring')

    if movies:
        await message.answer(movies, reply_markup=inline_menu)
    else:
        chronology = []
        for movie in all_movies.items():
            chronology.append(f'{movie[0]} -- {movie[1]}')
        
        result = 'Хронология Заклятия: \n\n' + '\n'.join(chronology)
        await message.answer(result, reply_markup=inline_menu)
        await set_cache_movies('conjuring', result)
