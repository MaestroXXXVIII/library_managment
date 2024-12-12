from dataclasses import asdict

from src.features.book.application.dtos import BookCreateDTO, BookOutDTO, BookUpdateDTO
from src.features.book.domain.entity import BookEntity
from src.features.book.domain.value_objects import CountAvailable


class BookMapper:
    @staticmethod
    def dto_to_entity(dto: BookCreateDTO) -> BookEntity:
        return BookEntity(
            title=dto.title,
            description=dto.description,
            author_id=dto.author_id,
            count_available=CountAvailable(dto.count_available),
        )

    @staticmethod
    def entity_to_dto(entity: BookEntity, author_name: str) -> BookOutDTO:
        return BookOutDTO(
            book_id=entity.book_id,
            title=entity.title,
            description=entity.description,
            author=author_name,
            count_available=entity.count_available.value,
        )

    @staticmethod
    def update_data(entity: BookEntity, updated_data: BookUpdateDTO) -> BookEntity:
        for field, value in asdict(updated_data).items():
            if value is not None and field != "count_available":
                setattr(entity, field, value)
        entity.count_available = CountAvailable(updated_data.count_available)

        return entity