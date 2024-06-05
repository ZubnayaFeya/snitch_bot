import asyncio
import contextlib
import logging

from aiogram import Bot, Dispatcher

from app.handlers import router
from config import logging_format, BOT_TOKEN


async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(router)

    try:
        await dp.start_polling(bot)#, allowed_updates=["chat_member"])
    except Exception as e:
        logging.error(f'[Exception] - {e}', exc_info=True)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format=logging_format)
    with contextlib.suppress(KeyboardInterrupt, SystemExit):
        asyncio.run(main())
