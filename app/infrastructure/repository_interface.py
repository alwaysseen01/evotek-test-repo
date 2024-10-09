from abc import ABC, abstractmethod
from typing import List

from select import select
from sqlalchemy import insert

from app.infrastructure.database import async_session_maker


class AbstractRepository(ABC):
    @abstractmethod
    async def get_all(self):
        raise NotImplementedError

    @abstractmethod
    async def get_by_id(self, given_id: int):
        raise NotImplementedError

    @abstractmethod
    async def add(self, data: dict):
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    async def get_all(self) -> List[model]:
        async with async_session_maker() as async_session:
            statement = select(self.model)
            result = await async_session.execute(statement)

            return result.scalars().all()

    async def get_by_id(self, given_id: int) -> model:
        async with async_session_maker() as async_session:
            statement = select(self.model).where(self.model.id == given_id)
            result = async_session.execute(statement)

            return result.scalars().first()

    async def add(self, data: dict) -> model:
        async with async_session_maker() as async_session:
            statement = insert(self.model).values(**data).returning(self.model)
            result = async_session.execute(statement)
            async_session.commit()

            return result.scalar_one()
