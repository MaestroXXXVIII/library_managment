from datetime import date
from typing import Annotated

from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter, Body, HTTPException, Response, status

from src.api.dtos.borrow_dtos import CreateBorrowDTO, ResponseBorrowDTO
from src.features.borrow.application.dtos import BorrowCreateDTO
from src.features.borrow.application.interactors import (
    CreateBorrowInteractor,
    GetBorrowByIdInteractor,
    GetBorrowsInteractor,
    ReturnBookInteractor,
)
from src.features.borrow.exceptions import BorrowNotFoundError, CreateBorrowError

borrow_router = APIRouter(route_class=DishkaRoute)


@borrow_router.post('/', response_model=None)
async def create_borrow(
    body: CreateBorrowDTO, interactor: FromDishka[CreateBorrowInteractor]
) -> Response:
    borrow = BorrowCreateDTO(**body.model_dump())

    try:
        await interactor.execute(borrow)
    except CreateBorrowError as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'{str(error)} с id={borrow.book_id}',
        )

    return Response(status_code=status.HTTP_201_CREATED)


@borrow_router.get('/{borrow_id}', response_model=ResponseBorrowDTO, status_code=status.HTTP_200_OK)
async def get_borrow_by_id(
    borrow_id: int, interactor: FromDishka[GetBorrowByIdInteractor]
) -> ResponseBorrowDTO:
    try:
        borrow = await interactor.execute(borrow_id)
    except BorrowNotFoundError as error:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'{str(error)} c id={borrow_id}',
        )
    return ResponseBorrowDTO(**borrow.__dict__)


@borrow_router.get('/', response_model=list[ResponseBorrowDTO], status_code=status.HTTP_200_OK)
async def get_borrows(interactor: FromDishka[GetBorrowsInteractor]) -> list[ResponseBorrowDTO]:
    try:
        borrows = await interactor.execute()
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error),
        )

    return [ResponseBorrowDTO(**borrow.__dict__) for borrow in borrows]


@borrow_router.patch(
    '/{borrow_id}/return', response_model=None, status_code=status.HTTP_204_NO_CONTENT
)
async def return_book_to_library(
    borrow_id: int,
    return_date: Annotated[date, Body()],
    interactor: FromDishka[ReturnBookInteractor],
) -> None:
    try:
        await interactor.execute(borrow_id, return_date)
    except BorrowNotFoundError as error:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'{str(error)} c id={borrow_id}',
        )
