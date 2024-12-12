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
    DeleteBookInteractor, ReduceCountAvailableInteractor, IncreaseCountAvailableInteractor
)
from src.features.borrow.application.interactors import (
    CreateBorrowInteractor,
    GetBorrowsInteractor,
    GetBorrowByIdInteractor,
    ReturnBookInteractor,
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
    reduce_count_available = provide(ReduceCountAvailableInteractor)
    increase_count_available = provide(IncreaseCountAvailableInteractor)


class BorrowInteractorProvider(Provider):
    scope = Scope.REQUEST

    create_borrow = provide(CreateBorrowInteractor)
    get_borrows = provide(GetBorrowsInteractor)
    get_borrow_by_id = provide(GetBorrowByIdInteractor)
    return_book = provide(ReturnBookInteractor)