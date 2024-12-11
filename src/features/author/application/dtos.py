from dataclasses import dataclass
from datetime import date


@dataclass
class BaseAuthorDTO:
    first_name: str
    last_name: str
    date_of_birth: date


@dataclass
class AuthorCreateDTO(BaseAuthorDTO):
    pass


@dataclass
class AuthorOutDTO(BaseAuthorDTO):
    author_id: int


@dataclass
class AuthorUpdateDTO(BaseAuthorDTO):
    first_name: str | None = None
    last_name: str | None = None
    date_of_birth: date | None = None
