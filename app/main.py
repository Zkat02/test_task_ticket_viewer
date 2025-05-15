from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.api.v1 import tickets
from app.db.base import Base
from app.db.session import engine
from app.db.models import *

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    await engine.dispose()

app = FastAPI(lifespan=lifespan)
app.include_router(tickets.router, prefix="/api/v1", tags=["tickets"])