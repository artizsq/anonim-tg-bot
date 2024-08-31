"""
Файл с функциями для создания клавиатур
"""

from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types

def cancel() -> InlineKeyboardBuilder:
    kb = InlineKeyboardBuilder()
    kb.add(types.InlineKeyboardButton(text="Отмена", callback_data="cancel"))
    return kb.as_markup()

def send_again(user_id) -> InlineKeyboardBuilder:
    kb = InlineKeyboardBuilder()
    kb.add(types.InlineKeyboardButton(text="Отправить ещё раз", callback_data="again_" + str(user_id)))
    return kb.as_markup()