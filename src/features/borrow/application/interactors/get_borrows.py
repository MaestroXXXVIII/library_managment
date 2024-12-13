from src.features.borrow.application.dtos import BorrowOutDTO
from src.features.borrow.application.mapper import BorrowMapper
from src.features.borrow.domain.abstract_repository import IBorrowRepository


class GetBorrowsInteractor:
    def __init__(self, borrow_repository: IBorrowRepository):
        self._repository = borrow_repository

    async def execute(self) -> list[BorrowOutDTO]:
        borrow_entities = await self._repository.get_all()
        try:
            borrows = [BorrowMapper.entity_to_dto(*borrow) for borrow in borrow_entities]
        except TypeError:
            raise

        return borrows
