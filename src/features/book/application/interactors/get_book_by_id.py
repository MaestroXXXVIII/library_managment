from src.features.book.application.dtos import BookOutDTO
from src.features.book.application.mapper import BookMapper
from src.features.book.domain.abstract_repository import IBookRepository
from src.features.book.exceptions import BookNotFoundError


class GetBookByIdInteractor:
    def __init__(self, book_repository: IBookRepository):
        self._repository = book_repository

    async def execute(self, book_id: int) -> BookOutDTO:
        book_entity = await self._repository.get_by_id(book_id=book_id)

        if not book_entity:
            raise BookNotFoundError()

        return BookMapper.entity_to_dto(*book_entity)
