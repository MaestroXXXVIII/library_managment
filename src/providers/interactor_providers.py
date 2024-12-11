from dishka import Provider, Scope, provide

from src.features.author.application.interactors import (
    CreateAuthorInteractor,
    GetAuthorByIdInteractor,
    GetAuthorsInteractor,
    UpdateAuthorInteractor,
    DeleteAuthorInteractor,
)
from src.features.book.application.interactors import (
    CreateBookInteractor,
    GetBookByIdInteractor,
    GetBooksInteractor,
    UpdateBookInteractor,
    DeleteBookInteractor
)


class AuthorInteractorProvider(Provider):
    scope = Scope.REQUEST

    create_author = provide(CreateAuthorInteractor)
    get_author_by_id = provide(GetAuthorByIdInteractor)
    get_authors = provide(GetAuthorsInteractor)
    update_author = provide(UpdateAuthorInteractor)
    delete_author = provide(DeleteAuthorInteractor)


class BookInteractorProvider(Provider):
    scope = Scope.REQUEST

    create_book = provide(CreateBookInteractor)
    get_book_by_id = provide(GetBookByIdInteractor)
    get_books = provide(GetBooksInteractor)
    update_book = provide(UpdateBookInteractor)
    delete_book = provide(DeleteBookInteractor)
