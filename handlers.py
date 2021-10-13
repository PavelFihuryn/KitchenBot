import os
from asyncio import sleep

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text, Command
from aiogram.types import Message


# from config import ADMIN_ID
from main import bot, dp
from parser import get_links

ADMIN_ID = os.environ["ADMIN_ID"]


async def send_to_admin(dp):
    await bot.send_message(chat_id=ADMIN_ID, text="Бот запущен")


@dp.message_handler(Command("start"), state=None)
async def start_bot(message: Message, state: FSMContext):
    item_list = get_links()
    user_id = message['from']['id']
    while True:
        for item in get_links():
            if item not in item_list:
                item_list.append(item)
                if len(item_list) > 50:
                    item_list.pop(0)
                await bot.send_message(chat_id=user_id, text=item)
        await sleep(300)


@dp.message_handler(Command("echo"), state=None)
async def start_bot(message: Message, state: FSMContext):
    user_id = message['from']['id']
    await bot.send_message(chat_id=user_id, text='Я жив, не ссы')
