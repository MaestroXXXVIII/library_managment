from src.features.borrow.domain.entity import BorrowEntity
from src.features.borrow.domain.value_objects import DateOfBorrow, DateOfReturn
from src.infrastructure.models import BorrowModel


class BorrowMapper:
    @staticmethod
    def entity_to_model(entity: BorrowEntity) -> BorrowModel:
        return BorrowModel(
            book_id=entity.book_id,
            reader_name=entity.reader_name,
            date_of_borrow=entity.date_of_borrow.value,
            date_of_return=(
                entity.date_of_return.value if entity.date_of_return is not None else None
            ),
        )

    @staticmethod
    def model_to_entity(model: BorrowModel) -> tuple[BorrowEntity, str]:
        return (
            BorrowEntity(
                book_id=model.book_id,
                reader_name=model.reader_name,
                date_of_borrow=DateOfBorrow(model.date_of_borrow),  # type: ignore
                date_of_return=DateOfReturn(model.date_of_return) if model.date_of_return else None,  # type: ignore
                borrow_id=model.id,
            ),
            model.book.title,
        )
