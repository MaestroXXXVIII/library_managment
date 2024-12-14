from src.features.book.domain.abstract_repository import IBookRepository
from src.features.book.domain.entity import BookEntity
from src.features.book.exceptions import AvailableCountBookError, BookNotFoundError


class IncreaseCountAvailableInteractor:
    def __init__(self, book_repository: IBookRepository):
        self._repository = book_repository

    async def execute(self, book_id: int) -> None:
        book = await self._get_book(book_id)

        try:
            book.count_available = book.count_available.increase_count_of_available()
        except AvailableCountBookError:
            raise

        await self._repository.change_count_available(book_id, book.count_available.value)

    async def _get_book(self, book_id: int) -> BookEntity:
        book_entity = await self._repository.get_by_id(book_id=book_id)
        if book_entity is None:
            raise BookNotFoundError

        return book_entity[0]
