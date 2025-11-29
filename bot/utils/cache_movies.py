import redis.asyncio

from bot.core.cache import CACHE, CACHE_TTL


cache_db = redis.asyncio.Redis(**CACHE)

async def get_cached_movies(key: str) -> str | None:
    try:
        movies = await cache_db.get(key)
        return movies
    except redis.asyncio.ConnectionError as e:
        return None
    except Exception as e:
        return None
    
async def set_cache_movies(key: str, values: str) -> bool:
    try:
        await cache_db.set(key, values, ex=CACHE_TTL)
        return True
    except redis.asyncio.ConnectionError as e:
        return False
    except Exception as e:
        return False
    