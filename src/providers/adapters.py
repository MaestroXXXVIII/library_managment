from typing import AsyncIterable

from dishka import Provider, Scope, provide
from environs import Env
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from src.config import Config, DbConfig
from src.features.author.domain.abstract_repository import IAuthorRepository
from src.features.book.domain.abstract_repository import IBookRepository
from src.features.borrow.domain.abstract_repository import IBorrowRepository
from src.infrastructure.repositories import (
    AuthorRepository,
    BookRepository,
    BorrowRepository,
)


class SqlalchemyProvider(Provider):
    @provide(scope=Scope.APP)
    def provide_engine(self, config: Config) -> AsyncEngine:
        return create_async_engine(config.db.construct_sqlalchemy_url)

    @provide(scope=Scope.APP)
    def provide_sessionmaker(self, engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
        return async_sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)

    @provide(scope=Scope.REQUEST, provides=AsyncSession)
    async def provide_session(
        self, sessionmaker: async_sessionmaker[AsyncSession]
    ) -> AsyncIterable[AsyncSession]:
        async with sessionmaker() as session:
            try:
                yield session
                await session.commit()
            except SQLAlchemyError:
                await session.rollback()
            finally:
                await session.close()


class ConfigProvider(Provider):
    @provide(scope=Scope.APP)
    def provide_config(self) -> Config:
        env = Env()
        env.read_env()
        return Config(
            db=DbConfig.from_env(env),
        )


class RepositoryProvider(Provider):
    scope = Scope.REQUEST

    author_provider = provide(AuthorRepository, provides=IAuthorRepository)
    book_provider = provide(BookRepository, provides=IBookRepository)
    borrow_provider = provide(BorrowRepository, provides=IBorrowRepository)
