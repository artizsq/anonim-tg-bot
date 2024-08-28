"""
Файл со всеми командами бота


"""


from aiogram import Bot, Router, types
from aiogram.filters import Command
from data.requests import get_code, get_messages, set_user, get_user
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


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
        await message.answer("ВЫ отправите код пользователю: " + str(user_id) + "\nДля этого отправьте мне сообщение: ")
        await state.set_state(Send.code)
    else:
        await message.answer(f"Код доступа: {await get_code(message.from_user.id)}")



@rt.message(Command("help"))
async def gelp_command(message: types.Message):
    await message.answer("Помощи не будет :)")


@rt.message(Command("profile"))
async def profile_command(message: types.Message):
    get, count = await get_messages(message.from_user.id)
    await message.answer(f"""
➖ Ваш профиль ➖

Ссылка для друзей: `https://t.me/bebra_tests_bot?start={await get_code(message.from_user.id)}`
Получено сообщений: {get}
Отправлено сообщений: {count}
""", parse_mode="Markdown")
    

@rt.message(Command("secret"))
async def secret_command(message: types.Message, bot: Bot):
    # sticker = types.InputFile("CAACAgIAAxkBAAELPwtmzwSHlG6STBmCM76SA0G8f-kzYQACrhsAApOEgUormxCo9FCQsTUE")
    await bot.send_sticker(chat_id=message.chat.id,
                           sticker="CAACAgIAAxkBAAEIDadmzwbpYOhQIQFmPS31IiX6giNr8wACrhsAApOEgUormxCo9FCQsTUE")
