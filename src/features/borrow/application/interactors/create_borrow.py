from src.features.book.application.interactors.reduce_count_available_book import (
    ReduceCountAvailableInteractor,
)
from src.features.book.exceptions import AvailableCountBookError, BookNotFoundError
from src.features.borrow.application.dtos import BorrowCreateDTO
from src.features.borrow.application.mapper import BorrowMapper
from src.features.borrow.domain.abstract_repository import IBorrowRepository
from src.features.borrow.exceptions import (
    BorrowAlreadyExistsError,
    CreateBorrowError,
    NotFoundBookForCreateBorrowed,
)


class CreateBorrowInteractor:
    def __init__(
        self,
        borrow_repository: IBorrowRepository,
        reduce_count_available_interactor: ReduceCountAvailableInteractor,
    ):
        self._repository = borrow_repository
        self._reduce_interactor = reduce_count_available_interactor

    async def execute(self, request_dto: BorrowCreateDTO) -> None:
        borrow_entity = BorrowMapper.dto_to_entity(request_dto)
        try:
            await self._repository.save(borrow_entity)
        except (BorrowAlreadyExistsError, NotFoundBookForCreateBorrowed) as error:
            raise CreateBorrowError(context=error) from error

        await self.reduce_available_count_book(request_dto.book_id)

    async def reduce_available_count_book(self, book_id: int) -> None:
        try:
            await self._reduce_interactor.execute(book_id)
        except (AvailableCountBookError, BookNotFoundError) as error:
            raise CreateBorrowError(context=error) from error
