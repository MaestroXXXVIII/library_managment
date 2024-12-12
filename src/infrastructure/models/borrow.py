from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Date, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .mixins import IntIdPkMixin

if TYPE_CHECKING:
    from .book import BookModel


class BorrowModel(Base, IntIdPkMixin):
    __tablename__ = 'borrows'

    book_id: Mapped[int] = mapped_column(ForeignKey('books.id'))
    reader_name: Mapped[str] = mapped_column(nullable=False)
    date_of_borrow: Mapped[Date] = mapped_column(Date, nullable=False)
    date_of_return: Mapped[Date | None] = mapped_column(Date)

    book: Mapped['BookModel'] = relationship('BookModel', back_populates='borrows')
