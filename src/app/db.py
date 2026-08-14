# from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

# from app.config import DATABASE_URL

# engine = create_async_engine(DATABASE_URL, echo=False)

# AsyncSessionLocal = async_sessionmaker(
#     engine,
#     expire_on_commit=False,
# )

from collections.abc import AsyncGenerator
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from app.config import get_settings


app_settings = get_settings()
engine = create_async_engine(get_settings.DATABASE_URL, echo=False)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False,
)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()