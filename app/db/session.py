import contextlib
from typing import AsyncIterator

from sqlalchemy.ext.asyncio import (AsyncSession, async_sessionmaker,
                                    create_async_engine)

from app.core.config import settings

engine = create_async_engine(settings.database_url)

AsyncSessionLocal = async_sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False, autocommit=False
)


@contextlib.asynccontextmanager
async def get_session() -> AsyncIterator[AsyncSession]:
    db = AsyncSessionLocal()
    try:
        yield db
        await db.commit()
    except Exception:
        await db.rollback()
        raise
    finally:
        await db.close()


async def get_db() -> AsyncIterator[AsyncSession]:
    async with get_session() as session:
        yield session
