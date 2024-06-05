import datetime

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, Chat

from utils.prepare import prepare_datetime

router = Router()

START_TIME = datetime.datetime.now()


@router.message(Command(commands=['status']))
async def get_status_bot(message: Message):
    print(message.from_user)
    uptime = datetime.datetime.now() - START_TIME
    text = f'Бот работает {prepare_datetime(uptime)}'
    await message.answer(text)

# @router.chat_member()
# async def check_subscription():
#     await bot.send_message(chat_id=from_user.id, text="текст сообщения")
