from abc import ABC, abstractmethod
from datetime import date

from .entity import BorrowEntity


class IBorrowRepository(ABC):
    """
    Interface repository for entity Borrow
    """
    @abstractmethod
    async def save(self, entity: BorrowEntity) -> None:
        """
        Save Borrow to database
        :param entity: Borrow entity to save
        :return: None
        """

    @abstractmethod
    async def get_by_id(self, borrow_id: int) -> tuple[BorrowEntity, str] | None:
        """
        Get a Borrow by his id
        :param borrow_id: Borrow id for the find
        :return: BorrowEntity or None if Borrow not found
        """

    @abstractmethod
    async def get_all(self) -> list[tuple[BorrowEntity, str]]:
        """
        Get a Borrows
        :return: list BorrowEntity
        """

    @abstractmethod
    async def set_return_date(self, borrow_id: int, return_date: date) -> None:
        """
        Set return date book
        :param borrow_id: id of the borrow
        :param return_date: date of book return
        :return: None
        """
