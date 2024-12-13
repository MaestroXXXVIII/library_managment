from src.features.book.application.dtos import BookUpdateDTO
from src.features.book.application.mapper import BookMapper
from src.features.book.domain.abstract_repository import IBookRepository
from src.features.book.domain.entity import BookEntity
from src.features.book.exceptions import UpdateBookError


class UpdateBookInteractor:
    def __init__(self, book_repository: IBookRepository):
        self._repository = book_repository

    async def execute(self, book_id: int, updated_data: BookUpdateDTO) -> None:
        existing_book = await self._get_existing_book(book_id)
        updated_book = self._map_to_updated_data(existing_book, updated_data)

        try:
            await self._repository.update(updated_book)
        except UpdateBookError:
            raise

    async def _get_existing_book(self, book_id: int) -> BookEntity:
        book_entity = await self._repository.get_by_id(book_id=book_id)
        return book_entity[0]

    @staticmethod
    def _map_to_updated_data(book: BookEntity, updated_data: BookUpdateDTO) -> BookEntity:
        try:
            updated_book = BookMapper.update_data(book, updated_data)
        except (ValueError, AttributeError) as error:
            raise UpdateBookError(context=error) from error

        return updated_book
