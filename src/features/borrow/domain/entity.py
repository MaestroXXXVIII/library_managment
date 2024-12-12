from dataclasses import dataclass, field
from datetime import timezone, datetime

from src.features.borrow.domain.value_objects import DateOfReturn, DateOfBorrow


@dataclass
class BorrowEntity:
    book_id: int
    reader_name: str
    date_of_borrow: DateOfBorrow = field(default_factory=lambda: DateOfBorrow(datetime.now(timezone.utc).date()))
    date_of_return: DateOfReturn | None = None
    borrow_id: int | None = None

    def __post_init__(self):
        self.validate_dates()

    def validate_dates(self):
        if not self.date_of_borrow:
            self.date_of_borrow = DateOfBorrow(datetime.now(timezone.utc).date())

        if self.date_of_return:
            if self.date_of_return.value < self.date_of_borrow.value:
                raise ValueError('Дата возврата не может быть раньше даты выдачи')
