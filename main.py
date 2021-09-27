import asyncio

from aiogram.contrib.fsm_storage.memory import MemoryStorage

from aiogram import Bot, Dispatcher, executor
# from config import BOT_TOKEN

import os

PORT = int(os.environ.get('PORT', 5000))
BOT_TOKEN = os.environ["BOT_TOKEN"]
ADMIN_ID = os.environ["ADMIN_ID"]

loop = asyncio.get_event_loop()
bot = Bot(BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, loop=loop, storage=MemoryStorage())

if __name__ == '__main__':
    from handlers import dp, send_to_admin

    loop = asyncio.get_event_loop()
    executor.start_polling(dp, on_startup=send_to_admin)
    executor.start_webhook(listen="0.0.0.0",
                           port=int(PORT),
                           url_path=BOT_TOKEN)
    executor.bot.setWebhook('https://kufarcitchenbot.herokuapp.com/' + BOT_TOKEN)
