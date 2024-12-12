from typing import Any, Tuple


class BorrowError(Exception):

    DEFAULT_MESSAGE = 'Ошибка при работе с выдачей'

    def __init__(self, context: Exception = None, message: str = None) -> None:
        self.context = context
        self.message = message or self.DEFAULT_MESSAGE
        self.args: Tuple[Any, ...] = (self.context, self.message)

    def __str__(self) -> str:
        if self.context:
            return f'{self.message} {self.context}'

        return self.message


class CreateBorrowError(BorrowError):
    DEFAULT_MESSAGE = 'Ошибка при создании записи о выдаче:'


class NotFoundBookForCreateBorrowed(BorrowError):
    DEFAULT_MESSAGE = 'Не найдена книга'


class BorrowAlreadyExistsError(BorrowError):
    DEFAULT_MESSAGE = 'Запись о выдаче уже существует'


class UpdateBorrowError(BorrowError):
    DEFAULT_MESSAGE = 'Ошибка при обновлении записи о выдаче'


class DeleteBorrowError(BorrowError):
    DEFAULT_MESSAGE = 'Ошибка при удалении записи о выдаче'


class BorrowNotFoundError(BorrowError):
    DEFAULT_MESSAGE = 'Не найдена запись о выдаче'
