from asyncio import sleep

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text, Command
from aiogram.types import Message


from config import admin_id
from main import bot, dp
from parser import get_links


async def send_to_admin(dp):
    await bot.send_message(chat_id=admin_id, text="Бот запущен")


@dp.message_handler(Command("start"), state=None)
async def start_bot(message: Message, state: FSMContext):
    kitchen_list = get_links()
    user_id = message['from']['id']
    while True:
        for kitchen in get_links():
            if kitchen not in kitchen_list:
                kitchen_list.append(kitchen)
                while len(kitchen_list) > 50:
                    kitchen_list.pop(0)
                await bot.send_message(chat_id=user_id, text=kitchen)
        await sleep(300)