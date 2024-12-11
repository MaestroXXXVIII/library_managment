from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter, HTTPException, Response, status

from src.api.dtos.book_dtos import CreateBookDTO, ResponseBookDTO, UpdateBookDTO
from src.features.book.application.dtos import BookCreateDTO, BookUpdateDTO
from src.features.book.application.interactors import (
    CreateBookInteractor,
    DeleteBookInteractor,
    GetBookByIdInteractor,
    GetBooksInteractor,
    UpdateBookInteractor,
)
from src.features.book.exceptions import (
    BookNotFoundError,
    CreateBookError,
    DeleteBookError,
    UpdateBookError,
)

book_router = APIRouter(route_class=DishkaRoute)


@book_router.post('/', response_model=None)
async def create_book(
    body: CreateBookDTO, interactor: FromDishka[CreateBookInteractor]
) -> Response:
    book = BookCreateDTO(**body.model_dump())

    try:
        await interactor.execute(book)
    except CreateBookError as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error),
        )

    return Response(status_code=status.HTTP_201_CREATED)


@book_router.get('/{book_id}', response_model=ResponseBookDTO, status_code=status.HTTP_200_OK)
async def get_book_by_id(
    book_id: int, interactor: FromDishka[GetBookByIdInteractor]
) -> ResponseBookDTO:
    try:
        book = await interactor.execute(book_id)
    except BookNotFoundError as error:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'{str(error)} c id={book_id}',
        )
    return ResponseBookDTO(**book.__dict__)


@book_router.get('/', response_model=list[ResponseBookDTO], status_code=status.HTTP_200_OK)
async def get_books(interactor: FromDishka[GetBooksInteractor]) -> list[ResponseBookDTO]:
    try:
        books = await interactor.execute()
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error),
        )

    return [ResponseBookDTO(**book.__dict__) for book in books]


@book_router.put('/{book_id}', response_model=None, status_code=status.HTTP_204_NO_CONTENT)
async def update_book(
    body: UpdateBookDTO, book_id: int, interactor: FromDishka[UpdateBookInteractor]
) -> None:
    updated_data = BookUpdateDTO(**body.model_dump(exclude_none=True))
    try:
        await interactor.execute(book_id, updated_data)
    except UpdateBookError as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error),
        )


@book_router.delete('/{book_id}', response_model=None, status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int, interactor: FromDishka[DeleteBookInteractor]) -> None:
    try:
        await interactor.execute(book_id)
    except DeleteBookError as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error),
        )
