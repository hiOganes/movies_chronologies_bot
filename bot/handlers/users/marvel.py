import aiohttp

from aiogram import Router, F
from aiogram.types import Message

from bot.utils.cache_movies import get_cached_movies, set_cache_movies
from bot.keyboards.inline import inline_menu


marvel_router = Router()

@marvel_router.message(F.text == 'Марвел')
async def get_marvel_chronology(message: Message):
    movies = await get_cached_movies('marvel')

    if movies:
        await message.answer(movies, reply_markup=inline_menu)
    else:
        url = "https://mcuapi.up.railway.app/api/v1/movies"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status != 200:
                    return f'API status code: {response.status}'
                else:
                    data = await response.json()

        chronology = []
        
        for movie in sorted(data.get("data", []), 
                            key=lambda x: x['chronology']):
            chronology.append(f'{movie['chronology']} -- {movie['title']}')
        
        result = 'Хронология Марвел: \n\n' + '\n'.join(chronology)
        await message.answer(result, reply_markup=inline_menu)
        await set_cache_movies('marvel', result)
