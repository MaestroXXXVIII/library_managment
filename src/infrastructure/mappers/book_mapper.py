from datetime import datetime
from src.features.book.domain.entity import BookEntity
from src.features.book.domain.value_objects import CountAvailable
from src.infrastructure.models import BookModel


class BookMapper:
    @staticmethod
    def entity_to_model(entity: BookEntity) -> BookModel:
        return BookModel(
            title=entity.title,
            description=entity.description,
            author_id=entity.author_id,
            count_available=entity.count_available.value,
        )

    @staticmethod
    def model_to_entity(model: BookModel) -> tuple[BookEntity, str]:
        return (
            BookEntity(
                book_id=model.id,
                title=model.title,
                description=model.description,
                author_id=model.author_id,
                count_available=CountAvailable(model.count_available),
            ),
            f'{model.author.first_name} {model.author.last_name}',
        )

    @staticmethod
    def entity_to_dict(entity: BookEntity) -> dict[str, str | datetime]:
        return {
            'title': entity.title,
            'description': entity.description,
            'author_id': entity.author_id,
            'count_available': entity.count_available.value
        }
