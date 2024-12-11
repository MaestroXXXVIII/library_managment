from src.features.book.domain.abstract_repository import IBookRepository
from src.features.book.exceptions import DeleteBookError


class DeleteBookInteractor:
    def __init__(self, book_repository: IBookRepository):
        self._repository = book_repository

    async def execute(self, book_id: int) -> None:
        try:
            await self._repository.delete(book_id=book_id)
        except DeleteBookError:
            raise