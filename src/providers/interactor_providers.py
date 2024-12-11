from dishka import Provider, Scope, provide

from src.features.author.application.interactors import (
    CreateAuthorInteractor,
    GetAuthorByIdInteractor,
    GetAuthorsInteractor,
    UpdateAuthorInteractor,
    DeleteAuthorInteractor,
)


class AuthorInteractorProvider(Provider):
    scope = Scope.REQUEST

    create_author = provide(CreateAuthorInteractor)
    get_author_by_id = provide(GetAuthorByIdInteractor)
    get_authors = provide(GetAuthorsInteractor)
    update_author = provide(UpdateAuthorInteractor)
    delete_author = provide(DeleteAuthorInteractor)
