from fastapi import FastAPI

from .author import author_router
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


__all__ = ('init_routes',)
