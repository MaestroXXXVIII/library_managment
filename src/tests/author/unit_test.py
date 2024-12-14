from datetime import date
from unittest.mock import AsyncMock

import pytest

from src.features.author.domain.entity import AuthorEntity
from src.features.author.domain.value_objects import DateOfBirth
from src.features.author.application.interactors import CreateAuthorInteractor
from src.features.author.application.dtos import AuthorCreateDTO
from src.features.author.exceptions import AuthorAlreadyExistsError, CreateAuthorError


@pytest.fixture
def author():
    return AuthorEntity(
        first_name="John",
        last_name="Doe",
        date_of_birth=DateOfBirth(date(1965, 10, 2)),
        _author_id=1
    )


class TestAuthorCreation:
    """Тесты для проверки корректного создания сущности Автора"""
    def test_author_creation(self, author: AuthorEntity) -> None:
        assert author.first_name == "John"
        assert author.last_name == "Doe"
        assert isinstance(author.date_of_birth, DateOfBirth)
        assert author.date_of_birth.value == date(1965, 10, 2)
        assert author._author_id == 1

    def test_author_missing_attributes(self, author: AuthorEntity) -> None:
        with pytest.raises(TypeError):
            AuthorEntity()


class TestDateOfBirth:
    """Тесты для проверки корректного указания даты рождения"""
    def test_valid_type_for_date_of_birth(self, author: AuthorEntity) -> None:
        author.date_of_birth = date(1970, 12, 3)

    @pytest.mark.parametrize(
        'date_of_birth', [
            '1965.10.2',
            1965102,
            ['1965', '10', '2']
        ]
    )
    def test_invalid_type_for_date_of_birth(self, author: AuthorEntity, date_of_birth) -> None:
        with pytest.raises(TypeError):
            author.date_of_birth = DateOfBirth(date_of_birth)


def test_change_author_id(author: AuthorEntity) -> None:
    with pytest.raises(AttributeError):
        author.author_id = 3


class TestAuthorCreateInteractor:
    """Тесты для проверки создания через интерактор"""
    @pytest.fixture
    def create_dto(self):
        return AuthorCreateDTO(
            first_name="John",
            last_name="Doe",
            date_of_birth=date(1965, 10, 12),
        )

    @pytest.mark.asyncio
    async def test_author_create_interactor(self, create_dto):
        mock_repo = AsyncMock()
        interactor = CreateAuthorInteractor(mock_repo)

        await interactor.execute(create_dto)

        mock_repo.save.assert_called_once()


    @pytest.mark.asyncio
    async def test_author_create_interactor_raises_create_author_error(self, create_dto):
        """Проверяем, что бросается правильное исключение"""
        mock_repo = AsyncMock()
        mock_repo.save.side_effect = AuthorAlreadyExistsError()
        interactor = CreateAuthorInteractor(mock_repo)

        with pytest.raises(CreateAuthorError):
            await interactor.execute(create_dto)

        mock_repo.save.assert_called_once()


    @pytest.mark.asyncio
    async def test_author_create_interactor_calls_save_with_correct_entity(self, create_dto, mocker):
        mock_repo = AsyncMock()
        interactor = CreateAuthorInteractor(mock_repo)

        mock_entity = mocker.Mock()
        mocker.patch(
            "src.features.author.application.mapper.AuthorMapper.dto_to_entity",
            return_value=mock_entity
        )

        await interactor.execute(create_dto)

        mock_repo.save.assert_called_once_with(mock_entity)
