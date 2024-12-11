from typing import Any, Tuple


class BookError(Exception):

    DEFAULT_MESSAGE = 'Ошибка при работе с книгой'

    def __init__(self, context: Exception = None, message: str = None) -> None:
        self.context = context
        self.message = message or self.DEFAULT_MESSAGE
        self.args: Tuple[Any, ...] = (self.context, self.message)

    def __str__(self) -> str:
        if self.context:
            return f'{self.message} {self.context}'

        return self.message


class AvailableCountBookError(BookError):
    DEFAULT_MESSAGE = 'Нет доступных книг'


class CreateBookError(BookError):
    DEFAULT_MESSAGE = 'Ошибка при создании книги'


class BookAlreadyExistsError(BookError):
    DEFAULT_MESSAGE = 'Книга уже существует'


class UpdateBookError(BookError):
    DEFAULT_MESSAGE = 'Ошибка при обновлении книги'


class DeleteBookError(BookError):
    DEFAULT_MESSAGE = 'Ошибка при удалении книги'


class BookNotFoundError(BookError):
    DEFAULT_MESSAGE = 'Не найдена книга'
