from src.features.author.application.dtos import AuthorOutDTO
from src.features.author.application.mapper import AuthorMapper
from src.features.author.domain.abstract_repository import IAuthorRepository


class GetAuthorsInteractor:
    def __init__(self, author_repository: IAuthorRepository):
        self._repository = author_repository

    async def execute(self) -> list[AuthorOutDTO]:
        author_entities = await self._repository.get_all()
        return [AuthorMapper.entity_to_dto(author) for author in author_entities]