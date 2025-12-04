import os

from dotenv import load_dotenv


load_dotenv()

CACHE = {
    'host':os.getenv('CACHE_HOST'),
    'port':os.getenv('CACHE_PORT'),
    'db':0,
    'decode_responses':True,
}

CACHE_TTL = 60 * 60 * 3