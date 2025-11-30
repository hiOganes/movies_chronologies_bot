from aiogram import Router, F
from aiogram.types import Message

from bot.utils.cache_movies import get_cached_movies, set_cache_movies
from bot.keyboards.inline import inline_menu


lord_of_the_rings_router = Router()

all_movies = {
    1: 'Властелин колец: Кольца власти (сериал)',
    2: 'Хоббит: Нежданное путешествие',
    3: 'Хоббит: Пустошь Смауга',
    4: 'Хоббит: Битва пяти воинств',
    5: 'Властелин колец: Братство кольца',
    6: 'Властелин колец: Две крепости',
    7: 'Властелин колец: Возвращение короля',
}

@lord_of_the_rings_router.message(F.text == 'Властелин колец')
async def lord_of_the_rings_chronology(message: Message):
    movies = await get_cached_movies('lord_of_the_rings')

    if movies:
        await message.answer(movies, reply_markup=inline_menu)
    else:
        chronology = []
        for movie in all_movies.items():
            chronology.append(f'{movie[0]} -- {movie[1]}')
        
        result = 'Хронология Властелина колец: \n\n' + '\n'.join(chronology)
        await message.answer(result, reply_markup=inline_menu)
        await set_cache_movies('lord_of_the_rings', result)
