from aiogram import Bot, Dispatcher
import asyncio
from data.models import async_main
from tg_bot import commands, handlers
import logging

logging.basicConfig(level=logging.INFO)

async def main():
    bot = Bot(token="")
    dp = Dispatcher()


    dp.include_routers(commands.rt, handlers.rt)
    await async_main()

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
