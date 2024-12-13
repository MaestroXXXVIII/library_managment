from typing import TYPE_CHECKING

from sqlalchemy import Date
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .mixins import IntIdPkMixin

if TYPE_CHECKING:
    from .book import BookModel


class AuthorModel(Base, IntIdPkMixin):
    __tablename__ = 'authors'

    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    date_of_birth: Mapped[Date] = mapped_column(Date, nullable=False)

    books: Mapped['BookModel'] = relationship('BookModel', back_populates='author')
