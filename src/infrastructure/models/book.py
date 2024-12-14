from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .mixins import IntIdPkMixin

if TYPE_CHECKING:
    from .author import AuthorModel
    from .borrow import BorrowModel


class BookModel(Base, IntIdPkMixin):
    __tablename__ = 'books'

    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    author_id: Mapped[int] = mapped_column(ForeignKey('authors.id', ondelete='CASCADE'))
    count_available: Mapped[int] = mapped_column(nullable=False)

    author: Mapped['AuthorModel'] = relationship('AuthorModel', back_populates='books')
    borrows: Mapped['BorrowModel'] = relationship('BorrowModel', back_populates='book')
