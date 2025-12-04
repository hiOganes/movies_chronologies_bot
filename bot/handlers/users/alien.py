from aiogram import Router, F
from aiogram.types import Message

from bot.utils.cache_movies import get_cached_movies, set_cache_movies
from bot.keyboards.inline import inline_menu


alien_router = Router()

all_movies = {
    1: 'Прометей',
    2: 'Чужой: Завет',
    3: 'Чужой: Земля (сериал)',
    4: 'Чужой: Ромул',
    5: 'Чужой',
    6: 'Чужие',
    7: 'Чужой 3',
    8: 'Чужой: Воскрешение',
    9: 'Чужой: Земля (сериал, сезон 2, в разработке)',
    10: 'Сиквел Чужой: Ромул (в разработке)',
    11: 'Третий приквел Чужой (возможный, Ридли Скотт)',
    12: 'Проект с Сигурни Уивер (в разработке)',
}

@alien_router.message(F.text == 'Чужой')
async def get_alien_chronology(message: Message):
    movies = await get_cached_movies('alien')

    if movies:
        await message.answer(movies, reply_markup=inline_menu)
    else:
        chronology = []
        for movie in all_movies.items():
            chronology.append(f'{movie[0]} -- {movie[1]}')
        
        result = 'Хронология Чужого: \n\n' + '\n'.join(chronology)
        await message.answer(result, reply_markup=inline_menu)
        await set_cache_movies('alien', result)