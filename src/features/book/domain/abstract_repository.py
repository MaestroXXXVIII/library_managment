from abc import ABC, abstractmethod

from .entity import BookEntity


class IBookRepository(ABC):
    """
    Interface repository for entity Book
    """
    @abstractmethod
    async def save(self, entity: BookEntity) -> None:
        """
        Save Book to database
        :param entity: Book entity to save
        :return: None
        """

    @abstractmethod
    async def get_by_id(self, book_id: int) -> tuple[BookEntity, str] | None:
        """
        Get a Book by his id
        :param book_id: Book id for the find
        :return: BookEntity or None if Book not found
        """

    @abstractmethod
    async def get_all(self) -> list[tuple[BookEntity, str]]:
        """
        Get a Books
        :return: list BookEntity
        """

    @abstractmethod
    async def update(self, book: BookEntity) -> BookEntity | None:
        """
        Update Book to database
        :param book: Book entity to update
        :return: Updated BookEntity
        """

    @abstractmethod
    async def delete(self, book_id: int) -> None:
        """
        Delete Book from database
        :param book_id: Book id for the delete
        :return: None because Book was deleted
        """
