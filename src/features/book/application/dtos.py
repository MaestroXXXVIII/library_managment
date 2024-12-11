from dataclasses import dataclass


@dataclass
class BaseBookDTO:
    title: str
    description: str
    count_available: int


@dataclass
class BookCreateDTO(BaseBookDTO):
    author_id: int


@dataclass
class BookOutDTO(BaseBookDTO):
    book_id: int
    author: str


@dataclass
class BookUpdateDTO:
    title: str | None = None
    description: str | None = None
    author_id: int | None = None
    count_available: int | None = None
