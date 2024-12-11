from dataclasses import asdict

from src.features.author.domain.entity import AuthorEntity
from src.features.author.domain.value_objects import DateOfBirth

from .dtos import AuthorCreateDTO, AuthorOutDTO, AuthorUpdateDTO


class AuthorMapper:
    @staticmethod
    def dto_to_entity(dto: AuthorCreateDTO) -> AuthorEntity:
        return AuthorEntity(
            first_name=dto.first_name,
            last_name=dto.last_name,
            date_of_birth=DateOfBirth(dto.date_of_birth),
        )

    @staticmethod
    def entity_to_dto(entity: AuthorEntity) -> AuthorOutDTO:
        return AuthorOutDTO(
            author_id=entity.author_id,
            first_name=entity.first_name,
            last_name=entity.last_name,
            date_of_birth=entity.date_of_birth.value,
        )

    @staticmethod
    def update_data(entity: AuthorEntity, updated_data: AuthorUpdateDTO) -> AuthorEntity:
        for field, value in asdict(updated_data).items():
            if value is not None:
                setattr(entity, field, value)

        return entity
