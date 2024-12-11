from dataclasses import dataclass
from typing import Self

from src.features.book.exceptions import AvailableCountBookError


@dataclass(frozen=True)
class CountAvailable:
    value: int

    def __post_init__(self):
        if self.value < 0:
            raise ValueError('Количество доступных книг не может быть меньше нуля')

    def check_count_of_available(self) -> int:
        return self.value

    def reduce_count_of_available(self) -> Self:
        if self.value == 0:
            raise AvailableCountBookError()
        return CountAvailable(self.value - 1)

    def increase_count_of_available(self) -> Self:
        return CountAvailable(self.value + 1)
