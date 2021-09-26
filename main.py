import asyncio

from aiogram.contrib.fsm_storage.memory import MemoryStorage

from aiogram import Bot, Dispatcher, executor
from config import BOT_TOKEN


loop = asyncio.get_event_loop()
bot = Bot(BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, loop=loop, storage=MemoryStorage())

if __name__ == '__main__':
    from handlers import dp, send_to_admin

    loop = asyncio.get_event_loop()
    # loop.create_task(see())
    executor.start_polling(dp, on_startup=send_to_admin)
