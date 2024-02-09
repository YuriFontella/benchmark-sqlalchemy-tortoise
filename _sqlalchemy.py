from fastapi import FastAPI
from contextlib import asynccontextmanager

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

DATABASE_URL = 'postgresql+asyncpg://postgres:123456@localhost:5432/blocks'

engine = create_async_engine(DATABASE_URL, echo=False, pool_pre_ping=True)
async_session = async_sessionmaker(engine, expire_on_commit=False)

class Base(AsyncAttrs, DeclarativeBase):
    pass

class Users(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    status: Mapped[bool]

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield
    await engine.dispose()


app = FastAPI(lifespan=lifespan)

@app.get('/data')
async def on_get_data():
    async with async_session() as session:
        query = await session.execute(select(Users).limit(1))
        results = query.scalar()

    return results

@app.get('/million')
async def on_get_million():
    async with async_session() as session:
        query = await session.execute(select(Users).limit(1000000))
        results = query.all()

    return len(results)