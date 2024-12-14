from dataclasses import dataclass, field
from datetime import datetime, timezone

from src.features.borrow.domain.value_objects import DateOfBorrow, DateOfReturn


@dataclass
class BorrowEntity:
    book_id: int
    reader_name: str
    date_of_borrow: DateOfBorrow = field(
        default_factory=lambda: DateOfBorrow(datetime.now(timezone.utc).date())
    )
    date_of_return: DateOfReturn | None = None
    borrow_id: int | None = None

    def __post_init__(self) -> None:
        self.validate_dates()

    def validate_dates(self) -> None:
        if not self.date_of_borrow:
            self.date_of_borrow = DateOfBorrow(datetime.now(timezone.utc).date())

        if self.date_of_return:
            if self.date_of_return.value < self.date_of_borrow.value:
                raise ValueError('Дата возврата не может быть раньше даты выдачи')
