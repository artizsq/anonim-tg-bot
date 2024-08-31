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

    base = "✉️ *Пришло новое сообщение!*\n\n"
    try:

        await add_messages_count(sender_id=message.from_user.id, receiver_id=user_id)

        await bot.send_message(user_id, text=base + message.text, parse_mode="Markdown")
        await message.answer(f"✅ Сообщение отправлено!", reply_markup=send_again(user_id=user_id))
        
        await state.clear()
    except Exception as e:
        await message.answer("⚠️❌ Произошла ошибка: `" + str(e) + "`\n\nПопробуйте ещё раз или напишите администратору (@ArtizSQ или @RegaaTG).", parse_mode="Markdown", reply_markup=cancel())

@rt.message(F.photo, Send.code)
async def send_photo(message: types.Message, state: FSMContext, bot: Bot):
    code = await state.get_data()
    user_id = code["user"]

    base = "✉️ *Пришло новое сообщение!*\n\n"

    try:
        text = base + str(message.caption if message.caption else "")

        await add_messages_count(sender_id=message.from_user.id, receiver_id=user_id)

        await bot.send_photo(user_id, photo=message.photo[-1].file_id, caption=text, parse_mode="Markdown")
        await message.answer(f"✅ Сообщение отправлено!", reply_markup=send_again(user_id=user_id))
        
        await state.clear()
    except Exception as e:
        await message.answer("⚠️❌ Произошла ошибка: `" + str(e) + "`\n\nПопробуйте ещё раз или напишите администратору (@ArtizSQ или @RegaaTG).", parse_mode="Markdown", reply_markup=cancel())


@rt.message(F.video, Send.code)
async def send_video(message: types.Message, state: FSMContext, bot: Bot):
    code = await state.get_data()
    user_id = code["user"]

    base = "*✉️ Пришло новое сообщение!*\n\n"

    try:
        text = base + str(message.caption if message.caption else "")

        await add_messages_count(sender_id=message.from_user.id, receiver_id=user_id)

        await bot.send_video(user_id, video=message.video.file_id, caption=text, parse_mode="Markdown")
        await message.answer(f"✅ Сообщение отправлено!", reply_markup=send_again(user_id=user_id))
        
        await state.clear()

    except Exception as e:
        await message.answer("⚠️❌ Произошла ошибка: `" + str(e) + "`\n\nПопробуйте ещё раз или напишите администратору (@ArtizSQ или @RegaaTG).", parse_mode="Markdown", reply_markup=cancel())



@rt.message(F.document, Send.code)
async def send_document(message: types.Message, state: FSMContext, bot: Bot):
    code = await state.get_data()
    user_id = code["user"]

    base = "*✉️ Пришло новое сообщение!*\n\n"

    try:
        text = base + str(message.caption if message.caption else "")

        await add_messages_count(sender_id=message.from_user.id, receiver_id=user_id)

        await bot.send_document(user_id, document=message.document.file_id, caption=text, parse_mode="Markdown")
        await message.answer(f"✅ Сообщение отправлено!", reply_markup=send_again(user_id=user_id))
        
        await state.clear()

    except Exception as e:
        await message.answer("⚠️❌ Произошла ошибка: `" + str(e) + "`\n\nПопробуйте ещё раз или напишите администратору (@ArtizSQ или @RegaaTG).", parse_mode="Markdown", reply_markup=cancel())




@rt.message(F.audio, Send.code)
async def send_audio(message: types.Message, state: FSMContext, bot: Bot):
    code = await state.get_data()
    user_id = code["user"]

    base = "*✉️ Пришло новое сообщение!*\n\n"

    try:
        text = base + str(message.caption if message.caption else "")

        await add_messages_count(sender_id=message.from_user.id, receiver_id=user_id)

        await bot.send_audio(user_id, audio=message.audio.file_id, caption=text, parse_mode="Markdown")
        await message.answer(f"✅ Сообщение отправлено!", reply_markup=send_again(user_id=user_id))
        
        await state.clear()

    except Exception as e:
        await message.answer("⚠️❌ Произошла ошибка: `" + str(e) + "`\n\nПопробуйте ещё раз или напишите администратору (@ArtizSQ или @RegaaTG).", parse_mode="Markdown", reply_markup=cancel())


@rt.message(F.voice, Send.code)
async def send_voice(message: types.Message, state: FSMContext, bot: Bot):
    code = await state.get_data()
    user_id = code["user"]

    base = "*✉️ Пришло новое сообщение!*\n\n"

    try:
        text = base + str(message.caption if message.caption else "")

        await add_messages_count(sender_id=message.from_user.id, receiver_id=user_id)

        
        await bot.send_voice(user_id, voice=message.voice.file_id, caption=text, parse_mode="Markdown")
        await message.answer(f"✅ Сообщение отправлено!", reply_markup=send_again(user_id=user_id))
        
        await state.clear()

    except Exception as e:
        await message.answer("⚠️❌ Произошла ошибка: `" + str(e) + "`\n\nПопробуйте ещё раз или напишите администратору (@ArtizSQ или @RegaaTG).", parse_mode="Markdown", reply_markup=cancel())




@rt.message(F.video_note, Send.code)
async def send_video_note(message: types.Message, state: FSMContext, bot: Bot):
    code = await state.get_data()
    user_id = code["user"]

    base = "*✉️ Пришло новое сообщение!*\n\n"

    try:
        text = base + str(message.caption if message.caption else "")

        await add_messages_count(sender_id=message.from_user.id, receiver_id=user_id)

        await bot.send_message(user_id, text=text, parse_mode="Markdown")
        await bot.send_video_note(user_id, video_note=message.video_note.file_id)
        await message.answer(f"✅ Сообщение отправлено!", reply_markup=send_again(user_id=user_id))
        
        await state.clear()

    except Exception as e:
        await message.answer("⚠️❌ Произошла ошибка: `" + str(e) + "`\n\nПопробуйте ещё раз или напишите администратору (@ArtizSQ или @RegaaTG).", parse_mode="Markdown", reply_markup=cancel())


@rt.message(F.sticker, Send.code)
async def send_sticker(message: types.Message, state: FSMContext, bot: Bot):
    code = await state.get_data()
    user_id = code["user"]

    base = "*✉️ Пришло новое сообщение!*\n\n"

    try:
        text = base + str(message.caption if message.caption else "")

        await add_messages_count(sender_id=message.from_user.id, receiver_id=user_id)

        await bot.send_message(user_id, text=text, parse_mode="Markdown")
        await bot.send_sticker(user_id, sticker=message.sticker.file_id)
        await message.answer(f"✅ Сообщение отправлено!", reply_markup=send_again(user_id=user_id))
        
        await state.clear()

    except Exception as e:
        await message.answer("⚠️❌ Произошла ошибка: `" + str(e) + "`\n\nПопробуйте ещё раз или напишите администратору (@ArtizSQ или @RegaaTG).", parse_mode="Markdown", reply_markup=cancel())
        



@rt.callback_query(F.data == "cancel")
async def cancel_button(callback: types.CallbackQuery, state: FSMContext):

    await callback.answer("Действие отменено!")
    await callback.message.delete()
    await state.clear()


@rt.callback_query(F.data.startswith("again_"))
async def send_again_button(callback: types.CallbackQuery, state: FSMContext):
    user_id = callback.data.split("_")[1]
    await state.update_data({"user": user_id})
    await callback.message.edit_text("👉 Введите сообщение, которое хотите отправить.\n\n🤖 Бот поддерживает следующие типы сообщений: `Текст, фото, видео, голосовые сообщения, видеосообщения, стикеры, документы, GIF.`", reply_markup=cancel(), parse_mode="Markdown")
    await state.set_state(Send.code)
