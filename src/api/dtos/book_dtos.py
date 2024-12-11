from pydantic import BaseModel


class CreateBookDTO(BaseModel):
    title: str
    description: str
    author_id: int
    count_available: int

class ResponseBookDTO(BaseModel):
    book_id: int
    title: str
    description: str
    author: str
    count_available: int


class UpdateBookDTO(BaseModel):
    title: str | None = None
    description: str | None = None
    author_id: int | None = None
    count_available: int | None = None