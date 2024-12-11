from src.features.book.application.dtos import BookOutDTO
from src.features.book.application.mapper import BookMapper
from src.features.book.domain.abstract_repository import IBookRepository


class GetBooksInteractor:
    def __init__(self, book_repository: IBookRepository):
        self._repository = book_repository

    async def execute(self) -> list[BookOutDTO]:
        book_entities = await self._repository.get_all()
        return [BookMapper.entity_to_dto(*book) for book in book_entities]