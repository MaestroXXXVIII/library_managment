from logging import warning

from sqlalchemy import delete, select, update
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload, selectinload

from src.features.book.domain.abstract_repository import IBookRepository
from src.features.book.domain.entity import BookEntity
from src.features.book.exceptions import BookAlreadyExistsError
from src.infrastructure.mappers.book_mapper import BookMapper
from src.infrastructure.models import BookModel


class BookRepository(IBookRepository):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def save(self, entity: BookEntity) -> None:
        book_model = BookMapper.entity_to_model(entity)
        self._session.add(book_model)
        try:
            await self._session.flush()
        except IntegrityError as error:
            warning(error)
            raise BookAlreadyExistsError()

    async def get_by_id(self, book_id: int) -> tuple[BookEntity, str] | None:
        query = select(BookModel).options(joinedload(BookModel.author)).filter_by(id=book_id)
        result = await self._session.execute(query)
        book = result.scalar_one_or_none()

        return BookMapper.model_to_entity(book) if book else None

    async def get_all(self) -> list[tuple[BookEntity, str]]:
        query = select(BookModel).options(selectinload(BookModel.author)).order_by(BookModel.id)
        result = await self._session.execute(query)
        return [BookMapper.model_to_entity(book) for book in result.scalars().all()]

    async def update(self, book: BookEntity) -> BookEntity | None:
        updated_data = BookMapper.entity_to_dict(book)
        stmt = update(BookModel).filter_by(id=book.book_id).values(**updated_data)
        await self._session.execute(stmt)
        return book

    async def delete(self, book_id: int) -> None:
        stmt = delete(BookModel).filter_by(id=book_id)
        await self._session.execute(stmt)

    async def change_count_available(self, book_id: int, count: int) -> None:
        stmt = update(BookModel).filter_by(id=book_id).values(count_available=count)
        await self._session.execute(stmt)
