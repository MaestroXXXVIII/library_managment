from src.features.author.application.dtos import AuthorCreateDTO
from src.features.author.application.mapper import AuthorMapper
from src.features.author.domain.abstract_repository import IAuthorRepository
from src.features.author.exceptions import AuthorAlreadyExistsError, CreateAuthorError


class CreateAuthorInteractor:
    def __init__(self, author_repository: IAuthorRepository):
        self._repository = author_repository

    async def execute(self, request_dto: AuthorCreateDTO) -> None:
        author_entity = AuthorMapper.dto_to_entity(request_dto)
        try:
            await self._repository.save(author_entity)
        except AuthorAlreadyExistsError as error:
            raise CreateAuthorError(context=error) from error
