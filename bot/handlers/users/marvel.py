import aiohttp

import redis.asyncio
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from bot.utils.cache_movies import get_cached_movies, set_cache_movies
from bot.core.cache import CACHE_TTL


marvel_router = Router()

@marvel_router.message(Command('marvel'))
async def get_marvel_chronology(message: Message):
    movies = await get_cached_movies('marvel')
    url = "https://mcuapi.up.railway.app/api/v1/movies"

    if movies:
        await message.answer(movies)
    else:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status != 200:
                    return f'API status code: {response.status}'
                else:
                    data = await response.json()

        movies = data.get("data", [])
        sorted_movies = sorted(movies, key=lambda x: x['chronology'])
        marvel_chronology = []
        
        for movie in sorted_movies:
            marvel_chronology.append(f'{movie['chronology']} -- ' 
                                     f'{movie['title']}')
        
        result = 'Хронология Марвел: \n\n' + '\n'.join(marvel_chronology)
        await message.answer(result)
        await set_cache_movies('marvel', result)