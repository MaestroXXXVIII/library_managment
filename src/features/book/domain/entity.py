from dataclasses import dataclass

from src.features.book.domain.value_objects import CountAvailable


@dataclass
class BookEntity:
    title: str
    description: str
    author_id: int
    count_available: CountAvailable
    book_id: int | None = None
