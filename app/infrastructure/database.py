import asyncio

from sqlalchemy.ext.asyncio import create_async_engine

from app.core.config import settings
from app.domain.models.models import metadata


async def async_main():
    async_engine = create_async_engine(settings.get_db_url(), echo=True)

    async with async_engine.begin() as conn:
        await conn.run_sync(metadata.drop_all)
        await conn.run_sync(metadata.create_all)

asyncio.run(async_main())
