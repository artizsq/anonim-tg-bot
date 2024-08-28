from aiogram.fsm.context import FSMContext
from aiogram import types, F, Router, Bot
from .commands import Send



rt = Router()


@rt.message(F.text, Send.code)
async def send_code(message: types.Message, state: FSMContext, bot: Bot):
    code = await state.get_data()
    user_id = code["user"]

    base = "✉️ Пришло новое сообщение!\n\n"
    try:
        await bot.send_message(user_id, text=base + message.text)
        await message.answer(f"Сообщение отправлено!")
    except Exception as e:
        await message.answer("Произошла ошибка: " + str(e))


    await state.clear()