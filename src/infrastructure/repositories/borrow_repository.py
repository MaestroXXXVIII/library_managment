from datetime import date
from logging import warning

from asyncpg.exceptions import ForeignKeyViolationError
from sqlalchemy import select, update
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload, selectinload

from src.features.borrow.domain.abstract_repository import IBorrowRepository
from src.features.borrow.domain.entity import BorrowEntity
from src.features.borrow.exceptions import (
    BorrowAlreadyExistsError,
    NotFoundBookForCreateBorrowed,
)
from src.infrastructure.mappers.borrow_mapper import BorrowMapper
from src.infrastructure.models import BorrowModel


class BorrowRepository(IBorrowRepository):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def save(self, entity: BorrowEntity) -> None:
        borrow_model = BorrowMapper.entity_to_model(entity)
        self._session.add(borrow_model)
        try:
            await self._session.flush()
        except IntegrityError as error:
            warning(error)
            if isinstance(error.orig.__cause__, ForeignKeyViolationError):
                raise NotFoundBookForCreateBorrowed()
            raise BorrowAlreadyExistsError()

    async def get_by_id(self, borrow_id: int) -> tuple[BorrowEntity, str] | None:
        query = select(BorrowModel).options(joinedload(BorrowModel.book)).filter_by(id=borrow_id)
        result = await self._session.execute(query)
        borrow = result.scalar_one_or_none()

        return BorrowMapper.model_to_entity(borrow) if borrow else None

    async def get_all(self) -> list[tuple[BorrowEntity, str]]:
        query = select(BorrowModel).options(selectinload(BorrowModel.book)).order_by(BorrowModel.id)
        result = await self._session.execute(query)
        return [BorrowMapper.model_to_entity(borrow) for borrow in result.scalars().all()]

    async def set_return_date(self, borrow_id: int, return_date: date) -> None:
        stmt = update(BorrowModel).filter_by(id=borrow_id).values(date_of_return=return_date)
        await self._session.execute(stmt)
