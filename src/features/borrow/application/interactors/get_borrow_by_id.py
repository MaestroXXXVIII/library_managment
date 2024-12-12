from src.features.borrow.application.dtos import BorrowOutDTO
from src.features.borrow.application.mapper import BorrowMapper
from src.features.borrow.domain.abstract_repository import IBorrowRepository
from src.features.borrow.exceptions import BorrowNotFoundError


class GetBorrowByIdInteractor:
    def __init__(self, borrow_repository: IBorrowRepository):
        self._repository = borrow_repository

    async def execute(self, borrow_id: int) -> BorrowOutDTO:
        borrow_entity = await self._repository.get_by_id(borrow_id=borrow_id)

        if not borrow_entity:
            raise BorrowNotFoundError()

        return BorrowMapper.entity_to_dto(*borrow_entity)
