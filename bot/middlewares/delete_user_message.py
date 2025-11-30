from aiogram import BaseMiddleware
from aiogram.types import Message

class DeleteUserMessageMiddleware(BaseMiddleware):
    async def __call__(self, handler, event: Message, data):
        try:
            await event.delete()
        except:
            pass 
        return await handler(event, data)