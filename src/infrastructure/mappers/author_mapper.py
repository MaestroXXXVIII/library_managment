from datetime import date

from src.features.author.domain.entity import AuthorEntity
from src.features.author.domain.value_objects import DateOfBirth
from src.infrastructure.models import AuthorModel


class AuthorMapper:
    @staticmethod
    def entity_to_model(entity: AuthorEntity) -> AuthorModel:
        return AuthorModel(
            first_name=entity.first_name,
            last_name=entity.last_name,
            date_of_birth=entity.date_of_birth.value,
        )

    @staticmethod
    def model_to_entity(model: AuthorModel) -> AuthorEntity:
        return AuthorEntity(
            _author_id=model.id,
            first_name=model.first_name,
            last_name=model.last_name,
            date_of_birth=DateOfBirth(model.date_of_birth),  # type: ignore
        )

    @staticmethod
    def entity_to_dict(entity: AuthorEntity) -> dict[str, str | date]:
        return {
            'first_name': entity.first_name,
            'last_name': entity.last_name,
            'date_of_birth': entity.date_of_birth.value,
        }
