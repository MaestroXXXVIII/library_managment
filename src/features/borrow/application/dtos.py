from dataclasses import dataclass
from datetime import date


@dataclass
class BaseBorrowDTO:
    reader_name: str
    date_of_borrow: date
    date_of_return: date | None


@dataclass
class BorrowCreateDTO(BaseBorrowDTO):
    book_id: int


@dataclass
class BorrowOutDTO(BaseBorrowDTO):
    borrow_id: int
    book: str


@dataclass
class BorrowUpdateDTO:
    date_of_return: date | None
