from dataclasses import asdict

from src.features.borrow.application.dtos import BorrowCreateDTO, BorrowOutDTO, BorrowUpdateDTO
from src.features.borrow.domain.entity import BorrowEntity
from src.features.borrow.domain.value_objects import DateOfBorrow, DateOfReturn


class BorrowMapper:
    @staticmethod
    def dto_to_entity(dto: BorrowCreateDTO) -> BorrowEntity:
        return BorrowEntity(
            book_id=dto.book_id,
            reader_name=dto.reader_name,
            date_of_borrow=DateOfBorrow(dto.date_of_borrow) if dto.date_of_borrow else None,
            date_of_return=DateOfReturn(dto.date_of_return) if dto.date_of_return else None,
        )

    @staticmethod
    def entity_to_dto(entity: BorrowEntity, book: str) -> BorrowOutDTO:
        return BorrowOutDTO(
            reader_name=entity.reader_name,
            book=book,
            date_of_borrow=entity.date_of_borrow.value,
            date_of_return=entity.date_of_return.value if entity.date_of_return else None,
            borrow_id=entity.borrow_id,
        )

    @staticmethod
    def update_data(entity: BorrowEntity, updated_data: BorrowUpdateDTO) -> BorrowEntity:
        for field, value in asdict(updated_data).items():
            if value is not None:
                setattr(entity, field, value)

        return entity