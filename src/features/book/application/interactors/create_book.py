from src.features.book.application.dtos import BookCreateDTO
from src.features.book.application.mapper import BookMapper
from src.features.book.domain.abstract_repository import IBookRepository
from src.features.book.exceptions import BookAlreadyExistsError, CreateBookError


class CreateBookInteractor:
    def __init__(self, book_repository: IBookRepository):
        self._repository = book_repository

    async def execute(self, request_dto: BookCreateDTO) -> None:
        book_entity = BookMapper.dto_to_entity(request_dto)
        try:
            await self._repository.save(book_entity)
        except BookAlreadyExistsError as error:
            raise CreateBookError(context=error) from error
