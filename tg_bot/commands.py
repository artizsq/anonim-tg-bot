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
async def start_command(message: types.Message, state: FSMContext, bot: Bot):
    await set_user(message.from_user.id)
    bot = await bot.get_me()

    if len(message.text) > 6:
        code = message.text[7:]

        user_id = await get_user(code)
        await state.update_data({"user": user_id})
        await message.answer("👉 Введите сообщение, которое хотите отправить.\n\n🤖 Бот поддерживает следующие типы сообщений: `Текст, фото, видео, голосовые сообщения, видеосообщения, стикеры, документы, GIF.`", reply_markup=cancel(), parse_mode="Markdown")
        await state.set_state(Send.code)
    else:
        link = f"https://t.me/{bot.username}?start={await get_code(message.from_user.id)}"
        await message.answer(f"""
🚀 Привет, друзья! 👋

🌟 Мы рады приветствовать вас в мире анонимных сообщений с нашим новым ботом “Анонимные сообщения | 149”! 
Здесь вы можете отправлять и получать анонимные сообщения, используя свою уникальную ссылку. Это идеальный способ выразить свои мысли и чувства без страха быть узнанным.

❓ Как это работает? Просто перейди в свой профиль скопируй свою ссылку отправь или же в свой канал или друзьям и начни общаться! Также и наоборот перейди по ссылке друга и пиши ему анонимно. Ваши сообщения будут видны только вам и человеку, которому вы их отправили. Никаких лишних глаз и ушей!(если что весь код есть на github-е)

🥸 Не упустите возможность поделиться своими мыслями и чувствами с миром, сохраняя при этом полную анонимность. Присоединяйтесь к нам уже сегодня и начните своё путешествие в мир анонимных сообщений! 

Твоя ссылка:
👉 `{link}`


""", parse_mode="Markdown")



@rt.message(Command("help"))
async def gelp_command(message: types.Message):
    await message.answer("Помощь будет")


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
