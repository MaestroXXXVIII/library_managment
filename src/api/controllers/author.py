from fastapi import APIRouter, HTTPException, status
from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute

from src.api.dtos.author_dtos import CreateAuthorDTO, ResponseAuthorDTO, UpdateAuthorDTO
from src.features.author.application.dtos import AuthorCreateDTO, AuthorUpdateDTO
from src.features.author.application.interactors import CreateAuthorInteractor, GetAuthorByIdInteractor, \
    GetAuthorsInteractor, UpdateAuthorInteractor, DeleteAuthorInteractor
from src.features.author.exceptions import CreateAuthorError, AuthorNotFoundError, UpdateAuthorError, DeleteAuthorError

author_router = APIRouter(route_class=DishkaRoute)


@author_router.post('/', response_model=None, status_code=status.HTTP_201_CREATED)
async def create_author(body: CreateAuthorDTO, interactor: FromDishka[CreateAuthorInteractor]) -> None:
    author = AuthorCreateDTO(**body.model_dump())
    try:
        await interactor.execute(author)
    except CreateAuthorError as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error),
        )


@author_router.get('/{author_id}', response_model=ResponseAuthorDTO, status_code=status.HTTP_200_OK)
async def get_author_by_id(author_id: int, interactor: FromDishka[GetAuthorByIdInteractor]) -> ResponseAuthorDTO:
    try:
        author = await interactor.execute(author_id)
    except AuthorNotFoundError as error:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'{str(error)} c id={author_id}',
        )
    return ResponseAuthorDTO(**author.__dict__)


@author_router.get('/', response_model=list[ResponseAuthorDTO], status_code=status.HTTP_200_OK)
async def get_authors(interactor: FromDishka[GetAuthorsInteractor]) -> list[ResponseAuthorDTO]:
    try:
        authors = await interactor.execute()
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error),
        )

    return [ResponseAuthorDTO(**author.__dict__) for author in authors]


@author_router.put('/{author_id}', response_model=None, status_code=status.HTTP_204_NO_CONTENT)
async def update_author(body: UpdateAuthorDTO, author_id: int, interactor: FromDishka[UpdateAuthorInteractor]) -> None:
    updated_data = AuthorUpdateDTO(**body.model_dump(exclude_none=True))
    try:
        await interactor.execute(author_id, updated_data)
    except UpdateAuthorError as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error),
        )

@author_router.delete('/{author_id}', response_model=None, status_code=status.HTTP_204_NO_CONTENT)
async def delete_author(author_id: int, interactor: FromDishka[DeleteAuthorInteractor]) -> None:
    try:
        await interactor.execute(author_id)
    except DeleteAuthorError as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error),
        )