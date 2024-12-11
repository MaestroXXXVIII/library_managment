from logging import warning

from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from src.features.author.domain.entity import AuthorEntity
from src.features.author.domain.abstract_repository import IAuthorRepository
from src.features.author.exceptions import AuthorAlreadyExistsError
from src.infrastructure.mappers.author_mapper import AuthorMapper
from src.infrastructure.models import AuthorModel


class AuthorRepository(IAuthorRepository):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def save(self, entity: AuthorEntity) -> None:
        author_model = AuthorMapper.entity_to_model(entity)
        self._session.add(author_model)
        try:
            await self._session.flush()
        except IntegrityError as error:
            warning(error)
            raise AuthorAlreadyExistsError()


    async def get_by_id(self, author_id: int) -> AuthorEntity | None:
        query = select(AuthorModel).filter_by(id=author_id)
        result = await self._session.execute(query)
        author = result.scalar_one_or_none()
        return AuthorMapper.model_to_entity(author) if author else None

    async def get_all(self) -> list[AuthorEntity]:
        query = select(AuthorModel).order_by(AuthorModel.id)
        result = await self._session.execute(query)
        return [AuthorMapper.model_to_entity(author) for author in result.scalars().all()]

    async def update(self, author: AuthorEntity) -> AuthorEntity | None:
        updated_data = AuthorMapper.entity_to_dict(author)
        print(updated_data)
        stmt = update(AuthorModel).filter_by(id=author.author_id).values(**updated_data)
        await self._session.execute(stmt)
        return author

    async def delete(self, author_id: int) -> None:
        stmt = delete(AuthorModel).filter_by(id=author_id)
        await self._session.execute(stmt)
