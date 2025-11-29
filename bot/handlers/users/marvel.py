import aiohttp

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from bot.utils.cache_movies import get_cached_movies, set_cache_movies


marvel_router = Router()

@marvel_router.message(Command('marvel'))
async def get_marvel_chronology(message: Message):
    movies = await get_cached_movies('marvel')

    if movies:
        await message.answer(movies)
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
        await message.answer(result)
        await set_cache_movies('marvel', result)