from src.features.author.domain.abstract_repository import IAuthorRepository
from src.features.author.exceptions import DeleteAuthorError


class DeleteAuthorInteractor:
    def __init__(self, author_repository: IAuthorRepository):
        self._repository = author_repository

    async def execute(self, author_id: int) -> None:
        try:
            await self._repository.delete(author_id=author_id)
        except DeleteAuthorError:
            raise
