from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.v1 import tickets
from app.db.base import Base
from app.db.models import *
from app.db.session import engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    await engine.dispose()


app = FastAPI(lifespan=lifespan)
app.include_router(tickets.router, prefix="/api/v1", tags=["tickets"])
