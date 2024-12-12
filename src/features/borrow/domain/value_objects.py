from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class Date:
    value: date

    def __post_init__(self):
        if not isinstance(self.value, date):
            raise TypeError(f'Неверный тип данных: {type(self.value)}.'
                            f'Ожидается date.')


@dataclass(frozen=True)
class DateOfBorrow(Date):
    pass


@dataclass(frozen=True)
class DateOfReturn(Date):
    pass
