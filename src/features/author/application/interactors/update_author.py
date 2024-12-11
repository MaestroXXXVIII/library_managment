from src.features.author.application.dtos import AuthorUpdateDTO
from src.features.author.application.mapper import AuthorMapper
from src.features.author.domain.abstract_repository import IAuthorRepository
from src.features.author.domain.entity import AuthorEntity
from src.features.author.exceptions import UpdateAuthorError


class UpdateAuthorInteractor:
    def __init__(self, author_repository: IAuthorRepository):
        self._repository = author_repository

    async def execute(self, author_id: int, updated_data: AuthorUpdateDTO) -> None:
        existing_author = await self._get_existing_author(author_id)
        updated_author = self._map_to_updated_data(existing_author, updated_data)

        try:
            await self._repository.update(updated_author)
        except UpdateAuthorError:
            raise

    async def _get_existing_author(self, author_id: int) -> AuthorEntity:
        author_entity = await self._repository.get_by_id(
            author_id=author_id
        )
        return author_entity

    @staticmethod
    def _map_to_updated_data(author: AuthorEntity, updated_data: AuthorUpdateDTO) -> AuthorEntity:
        try:
            updated_author = AuthorMapper.update_data(author, updated_data)
        except (ValueError, AttributeError) as error:
            raise UpdateAuthorError(context=error) from error

        return updated_author
