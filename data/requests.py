import os

from aiogram import Bot
from .models import User, async_session
from sqlalchemy import select, log



async def set_user(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        if not user:
            new_user = User(tg_id=tg_id, 
                            code=os.urandom(10).hex())
            session.add(new_user)

            await session.commit()
        

async def get_code(tg_id):
    async with async_session() as session:
        code = await session.scalar(select(User).where(User.tg_id == tg_id))
        return code.code
    

async def get_user(code):
    async with async_session() as session:
        _user = await session.scalar(select(User).where(User.code == code))
        if _user is None:
            raise ValueError("User with code {} not found".format(code))
        return _user.tg_id
        

async def get_messages(tg_id):
    async with async_session() as session:
        count = await session.scalar(select(User.message_count).where(User.tg_id == tg_id))
        get = await session.scalar(select(User.message_get).where(User.tg_id == tg_id))

        return count, get
    
async def add_messages_count(sender_id, receiver_id):
    async with async_session() as session:
        sender = await session.scalar(select(User).where(User.tg_id == sender_id))
        sender.message_count += 1

        receiver = await session.scalar(select(User).where(User.tg_id == receiver_id))
        receiver.message_get += 1
        
        await session.commit()


















