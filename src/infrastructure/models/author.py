from datetime import datetime

from sqlalchemy import Date
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .mixins import IntIdPkMixin


class AuthorModel(Base, IntIdPkMixin):
    __tablename__ = 'authors'

    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    date_of_birth: Mapped[Date] = mapped_column(Date, nullable=False)
