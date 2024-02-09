from fastapi import FastAPI
from contextlib import asynccontextmanager

from tortoise import Tortoise, fields
from tortoise.models import Model
from tortoise.connection import connections

DB_URL = 'asyncpg://postgres:123456@localhost:5432/blocks'

class Users(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    status = fields.BooleanField()

@asynccontextmanager
async def lifespan(app: FastAPI):
    await Tortoise.init(db_url=DB_URL, modules={'models': ['_tortoise']})
    await Tortoise.generate_schemas()

    yield
    await connections.close_all()


app = FastAPI(lifespan=lifespan)

@app.get('/data')
async def on_get_data():
    return await Users.first()

@app.get('/million')
async def on_get_million():
    data = await Users.all().limit(1000000)
    return len(data)