from dataclasses import dataclass

from .value_objects import DateOfBirth


@dataclass
class AuthorEntity:
    first_name: str
    last_name: str
    date_of_birth: DateOfBirth
    _author_id: int | None = None

    @property
    def author_id(self) -> int:
        return self._author_id

    @author_id.setter
    def author_id(self, new_id: int) -> None:
        if self._author_id is not None:
            raise AttributeError('Id автора уже установлено')

        self._author_id = new_id
