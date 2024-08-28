from aiogram.fsm.context import FSMContext
from aiogram import types, F, Router, Bot
from .commands import Send
from .key import cancel, send_again
from data.requests import add_messages_count



rt = Router()


@rt.message(F.text, Send.code)
async def send_code(message: types.Message, state: FSMContext, bot: Bot):
    code = await state.get_data()
    user_id = code["user"]

    base = "✉️ **Пришло новое сообщение!**\n\n"
    try:

        await add_messages_count(sender_id=message.from_user.id, receiver_id=user_id)

        await bot.send_message(user_id, text=base + message.text, parse_mode="Markdown")
        await message.answer(f"✅ Сообщение отправлено!", reply_markup=send_again())
        
        await state.clear()
    except Exception as e:
        await message.answer("⚠️❌ Произошла ошибка: " + str(e) + "\n\nПопробуйте ещё раз или напишите администратору (@ArtizSQ или @RegaTG).")






@rt.callback_query(F.data == "cancel")
async def cancel_button(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer("Действие отменено!")
    await callback.message.delete()
    await state.clear()