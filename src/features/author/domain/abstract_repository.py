from abc import ABC, abstractmethod

from .entity import AuthorEntity


class IAuthorRepository(ABC):
    """
    Interface repository for entity Author
    """
    @abstractmethod
    async def save(self, entity: AuthorEntity) -> None:
        """
        Save Author to database
        :param entity: Author entity to save
        :return: None
        """

    @abstractmethod
    async def get_by_id(self, author_id: int) -> AuthorEntity | None:
        """
        Get an Author by his id
        :param author_id: Author id for the find
        :return: AuthorEntity or None if Author not found
        """

    @abstractmethod
    async def get_all(self) -> list[AuthorEntity]:
        """
        Get an Authors
        :return: list AuthorEntity
        """

    @abstractmethod
    async def update(self, author: AuthorEntity) -> AuthorEntity | None:
        """
        Update Author to database
        :param author: Author entity to update
        :return: Updated AuthorEntity
        """

    @abstractmethod
    async def delete(self, author_id: int) -> None:
        """
        Delete Author from database
        :param author_id: Author id for the delete
        :return: None because Author was deleted
        """
