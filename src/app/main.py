import asyncio
import sys

from app.db import engine
from app.models import Base


async def drop_db():
    async with engine.begin() as conn:
        print("🔥 Dropping all database tables...")
        await conn.run_sync(Base.metadata.drop_all)
        print("✅ All tables dropped.")


async def init_db():
    async with engine.begin() as conn:
        print("🛠️  Creating database tables...")
        await conn.run_sync(Base.metadata.create_all)
        print("✅ Tables created.")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""

    if cmd == "drop-db":
        asyncio.run(drop_db())
    elif cmd == "init-db":
        asyncio.run(init_db())
    else:
        print("Usage: python -m app.main [drop-db | init-db]")