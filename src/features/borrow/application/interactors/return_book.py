from datetime import date

from src.features.book.application.interactors import IncreaseCountAvailableInteractor
from src.features.borrow.domain.abstract_repository import IBorrowRepository
from src.features.borrow.domain.entity import BorrowEntity
from src.features.borrow.exceptions import BorrowNotFoundError


class ReturnBookInteractor:
    def __init__(
        self,
        borrow_repository: IBorrowRepository,
        increase_count_available_interactor: IncreaseCountAvailableInteractor,
    ):
        self._repository = borrow_repository
        self._increase_interactor = increase_count_available_interactor

    async def execute(self, borrow_id: int, return_date: date) -> None:
        borrow = await self._get_borrow(borrow_id)
        await self._repository.set_return_date(borrow_id, return_date)
        await self._increase_count(borrow.book_id)

    async def _get_borrow(self, borrow_id: int) -> BorrowEntity:
        borrow = await self._repository.get_by_id(borrow_id)

        if borrow is None:
            raise BorrowNotFoundError

        return borrow[0]

    async def _increase_count(self, book_id: int) -> None:
        await self._increase_interactor.execute(book_id)
