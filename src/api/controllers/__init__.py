from fastapi import FastAPI

from .author import author_router
from .book import book_router
from .borrow import borrow_router
from .health_check import router


def init_routes(app: FastAPI) -> None:
    prefix: str = '/api/v1'
    app.include_router(
        router=router,
        prefix=f'{prefix}/health-check',
        tags=['Test'],
    )
    app.include_router(
        router=author_router,
        prefix=f'{prefix}/authors',
        tags=['Authors'],
    )
    app.include_router(
        router=book_router,
        prefix=f'{prefix}/books',
        tags=['Books'],
    )
    app.include_router(
        router=borrow_router,
        prefix=f'{prefix}/borrows',
        tags=['Borrows'],
    )


__all__ = ('init_routes',)
