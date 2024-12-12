from datetime import date

from pydantic import BaseModel


class CreateBorrowDTO(BaseModel):
    book_id: int
    reader_name: str
    date_of_borrow: date | None = None
    date_of_return: date | None = None


class ResponseBorrowDTO(BaseModel):
    borrow_id: int
    book: str
    reader_name: str
    date_of_borrow: date
    date_of_return: date | None


class UpdateBorrowDTO(BaseModel):
    date_of_return: date
