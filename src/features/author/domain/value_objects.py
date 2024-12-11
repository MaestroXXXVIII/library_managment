from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class DateOfBirth:
    value: date

    def __post_init__(self):
        if not isinstance(self.value, date):
            raise TypeError(f'Неверный тип данных: {type(self.value)}.'
                            f'Ожидается datetime.')
