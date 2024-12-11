from src.features.author.application.dtos import AuthorOutDTO
from src.features.author.application.mapper import AuthorMapper
from src.features.author.domain.abstract_repository import IAuthorRepository
from src.features.author.exceptions import AuthorNotFoundError


class GetAuthorByIdInteractor:
    def __init__(self, author_repository: IAuthorRepository):
        self._repository = author_repository

    async def execute(self, author_id: int) -> AuthorOutDTO:
        author_entity = await self._repository.get_by_id(author_id=author_id)

        if not author_entity:
            raise AuthorNotFoundError()

        return AuthorMapper.entity_to_dto(author_entity)
