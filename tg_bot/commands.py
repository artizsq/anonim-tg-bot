"""
Файл со всеми командами бота
"""


from aiogram import Bot, Router, types
from aiogram.filters import Command
from data.requests import get_code, get_messages, set_user, get_user
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from .key import cancel


class Send(StatesGroup):
    code = State()
    user = State()

rt = Router()

@rt.message(Command("start"))
async def start_command(message: types.Message, state: FSMContext):
    await set_user(message.from_user.id)

    if len(message.text) > 6:
        code = message.text[7:]

        user_id = await get_user(code)
        await state.update_data({"user": user_id})
        await message.answer("👉 Введите сообщение, которое хотите отправить.\n\n🤖 Бот поддерживает следующие типы сообщений: `текст, фото, видео, документы, GIF, стикер, голосовые сообщения, видеосообщения.`", reply_markup=cancel(), parse_mode="Markdown")
        await state.set_state(Send.code)
    else:
        await message.answer(f"Код доступа: {await get_code(message.from_user.id)}")



@rt.message(Command("help"))
async def gelp_command(message: types.Message):
    await message.answer("Помощи не будет :)")


@rt.message(Command("profile"))
async def profile_command(message: types.Message, bot: Bot):
    get, count = await get_messages(message.from_user.id)
    _bot = await bot.get_me()
    await message.answer(f"""
➖➖➖➖➖➖➖➖➖➖➖
*Информация о вас:*
 
👤 Username: @{message.from_user.username}
ℹ️ Id: {message.from_user.id}

*Сообщения:*       
📥 Кол-во полученных: {get}
📤 Кол-во отправленных: {count}
                         
🔗 Твоя ссылка: 
👉`https://t.me/{_bot.username}?start={await get_code(message.from_user.id)}`
➖➖➖➖➖➖➖➖➖➖➖
""", parse_mode="Markdown")
    

@rt.message(Command("secret"))
async def secret_command(message: types.Message, bot: Bot):
    # sticker = types.InputFile("CAACAgIAAxkBAAELPwtmzwSHlG6STBmCM76SA0G8f-kzYQACrhsAApOEgUormxCo9FCQsTUE")
    await bot.send_sticker(chat_id=message.chat.id,
                           sticker="CAACAgIAAxkBAAEIDadmzwbpYOhQIQFmPS31IiX6giNr8wACrhsAApOEgUormxCo9FCQsTUE")
