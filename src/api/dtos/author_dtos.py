from datetime import date

from pydantic import BaseModel


class CreateAuthorDTO(BaseModel):
    first_name: str
    last_name: str
    date_of_birth: date


class ResponseAuthorDTO(BaseModel):
    author_id: int
    first_name: str
    last_name: str
    date_of_birth: date


class UpdateAuthorDTO(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    date_of_birth: date | None = None
