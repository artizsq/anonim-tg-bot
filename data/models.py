from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.types import BigInteger
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine


engine = create_async_engine(url="sqlite+aiosqlite:///db.sqlite3")

async_session = async_sessionmaker(engine)



class Base(AsyncAttrs, DeclarativeBase):
    pass



class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)
    message_count: Mapped[int] = mapped_column(default=0)
    message_get: Mapped[int] = mapped_column(default=0)

    code: Mapped[str] = mapped_column()



async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
