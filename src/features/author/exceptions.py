from typing import Any, Tuple


class AuthorError(Exception):

    DEFAULT_MESSAGE = 'Ошибка при работе с Автором'

    def __init__(self, context: Exception = None, message: str = None) -> None:
        self.context = context
        self.message = message or self.DEFAULT_MESSAGE
        self.args: Tuple[Any, ...] = (self.context, self.message)

    def __str__(self) -> str:
        if self.context:
            return f'{self.message} {self.context}'

        return self.message


class CreateAuthorError(AuthorError):
    DEFAULT_MESSAGE = 'Ошибка при создании автора'


class AuthorAlreadyExistsError(AuthorError):
    DEFAULT_MESSAGE = 'Автор уже существует'


class UpdateAuthorError(AuthorError):
    DEFAULT_MESSAGE = 'Ошибка при обновлении автора'


class DeleteAuthorError(AuthorError):
    DEFAULT_MESSAGE = 'Ошибка при удалении автора'


class AuthorNotFoundError(AuthorError):
    DEFAULT_MESSAGE = 'Не найден автор'
