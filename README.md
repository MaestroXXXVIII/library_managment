# Library Management API

## Описание

Library Management API - это REST API для управления библиотечным каталогом. Проект разработан с использованием FastAPI и SQLAlchemy и предоставляет функционал для работы с книгами, авторами и выдачами книг читателям.
Проект разрабатывался с применением принципов чистой архитектуры и DDD.

## Функциональность

API реализует следующие возможности:

### Управление авторами
- **Создание автора** (POST `/authors`)
- **Получение списка авторов** (GET `/authors`)
- **Получение информации об авторе по ID** (GET `/authors/{id}`)
- **Обновление информации об авторе** (PUT `/authors/{id}`)
- **Удаление автора** (DELETE `/authors/{id}`)

### Управление книгами
- **Добавление книги** (POST `/books`)
- **Получение списка книг** (GET `/books`)
- **Получение информации о книге по ID** (GET `/books/{id}`)
- **Обновление информации о книге** (PUT `/books/{id}`)
- **Удаление книги** (DELETE `/books/{id}`)

### Управление выдачами
- **Создание записи о выдаче книги** (POST `/borrows`)
- **Получение списка всех выдач** (GET `/borrows`)
- **Получение информации о выдаче по ID** (GET `/borrows/{id}`)
- **Завершение выдачи** (PATCH `/borrows/{id}/return`) с указанием даты возврата

### Бизнес-логика
- Проверка наличия доступных экземпляров книги при создании записи о выдаче
- Уменьшение количества доступных экземпляров книги при выдаче
- Увеличение количества доступных экземпляров книги при возврате
- Возврат ошибки при попытке выдать недоступную книгу

## Структура проекта

```plaintext
├── alembic.ini
├── docker-compose.yaml
├── Dockerfile
├── justfile
├── poetry.lock
├── postgres
│   └── data
├── pyproject.toml
├── pytest.ini
├── README.md
├── ruff.toml
└── src
    ├── api
    │   ├── controllers
    │   │   ├── author.py
    │   │   ├── book.py
    │   │   ├── borrow.py
    │   │   ├── health_check.py
    │   │   └── __init__.py
    │   ├── dtos
    │   │   ├── author_dtos.py
    │   │   ├── book_dtos.py
    │   │   ├── borrow_dtos.py
    │   │   └── __init__.py
    │   ├── __init__.py
    │   └── middlewares
    │       ├── __init__.py
    │       └── logging.py
    ├── config.py
    ├── features
    │   ├── author
    │   │   ├── application
    │   │   │   ├── dtos.py
    │   │   │   ├── __init__.py
    │   │   │   ├── interactors
    │   │   │   │   ├── create_author.py
    │   │   │   │   ├── delete_author.py
    │   │   │   │   ├── get_author_by_id.py
    │   │   │   │   ├── get_authors.py
    │   │   │   │   ├── __init__.py
    │   │   │   │   └── update_author.py
    │   │   │   └── mapper.py
    │   │   ├── domain
    │   │   │   ├── abstract_repository.py
    │   │   │   ├── entity.py
    │   │   │   ├── __init__.py
    │   │   │   └── value_objects.py
    │   │   ├── exceptions.py
    │   │   └── __init__.py
    │   ├── book
    │   │   ├── application
    │   │   │   ├── dtos.py
    │   │   │   ├── __init__.py
    │   │   │   ├── interactors
    │   │   │   │   ├── create_book.py
    │   │   │   │   ├── delete_book.py
    │   │   │   │   ├── get_book_by_id.py
    │   │   │   │   ├── get_books.py
    │   │   │   │   ├── increase_count_available_book.py
    │   │   │   │   ├── __init__.py
    │   │   │   │   ├── reduce_count_available_book.py
    │   │   │   │   └── update_book.py
    │   │   │   └── mapper.py
    │   │   ├── domain
    │   │   │   ├── abstract_repository.py
    │   │   │   ├── entity.py
    │   │   │   ├── __init__.py
    │   │   │   └── value_objects.py
    │   │   ├── exceptions.py
    │   │   └── __init__.py
    │   ├── borrow
    │   │   ├── application
    │   │   │   ├── dtos.py
    │   │   │   ├── __init__.py
    │   │   │   ├── interactors
    │   │   │   │   ├── create_borrow.py
    │   │   │   │   ├── get_borrow_by_id.py
    │   │   │   │   ├── get_borrows.py
    │   │   │   │   ├── __init__.py
    │   │   │   │   └── return_book.py
    │   │   │   └── mapper.py
    │   │   ├── domain
    │   │   │   ├── abstract_repository.py
    │   │   │   ├── entity.py
    │   │   │   ├── __init__.py
    │   │   │   └── value_objects.py
    │   │   ├── exceptions.py
    │   │   └── __init__.py
    │   └── __init__.py
    ├── infrastructure
    │   ├── __init__.py
    │   ├── mappers
    │   │   ├── author_mapper.py
    │   │   ├── book_mapper.py
    │   │   ├── borrow_mapper.py
    │   │   └── __init__.py
    │   ├── migrations
    │   │   ├── env.py
    │   │   ├── __init__.py
    │   │   ├── script.py.mako
    │   │   └── versions
    │   │       ├── 2024_12_10_1320-247cf0e5db56_.py
    │   │       ├── 2024_12_11_1213-5a3357b9c3aa_.py
    │   │       ├── 2024_12_12_1058-37c9165a239b_.py
    │   │       └── __init__.py
    │   ├── models
    │   │   ├── author.py
    │   │   ├── base.py
    │   │   ├── book.py
    │   │   ├── borrow.py
    │   │   ├── __init__.py
    │   │   └── mixins.py
    │   └── repositories
    │       ├── author_repository.py
    │       ├── book_repository.py
    │       ├── borrow_repository.py
    │       └── __init__.py
    ├── __init__.py
    ├── main.py
    ├── providers
    │   ├── adapters.py
    │   ├── __init__.py
    │   └── interactor_providers.py
    ├── tests
    │   ├── author
    │   │   ├── __init__.py
    │   │   ├── integration_test.py
    │   │   └── unit_test.py
    │   └── __init__.py
    └── utils
        ├── __init__.py
        └── log
            ├── configuration.py
            ├── __init__.py
            └── setup.py

```

## Установка и запуск

### Локальный запуск
1. Скопируйте файл `.env.template` и переименуйте его в `.env` для локального запуска параметр DB_HOST=localhost.
2. Убедитесь, что все зависимости установлены через [Poetry](https://python-poetry.org/):
   ```bash
   poetry install
   ```
3. Установите переменную окружения `PYTHONPATH` для корректной работы импортов:
   ```bash
   export PYTHONPATH=$(pwd)
   ```
4. Запустите приложение:
   ```bash
   poetry run python src/main.py
   ```
5. Для запуска через `uvicorn`:
   ```bash
   poetry run uvicorn src.main:create_app --reload
   ```

### Запуск с использованием Docker
1. Скопируйте файл `.env.template` и переименуйте его в `.env`. Убедитесь, что переменная `DB_HOST` установлена на `postgres`.
2. Запустите контейнеры:
   ```bash
   docker-compose up --build
   ```

## Зависимости

Основные зависимости:
- **FastAPI**: ^0.115.0
- **SQLAlchemy**: 2.0.25
- **asyncpg**: ^0.29.0
- **Alembic**: ^1.13.1
- **Dishka**: ^1.2.0
- **Uvicorn**: ^0.30.6

Инструменты для разработки:
- **pytest**: ^8.2.0
- **black**: ^24.3.0
- **ruff**: ^0.6.6
- **mypy**: ^1.8.0
- и другие.

## Тестирование

Для запуска тестов используйте:
```bash
poetry run pytest
```

## Документация API

После запуска приложения документация будет доступна по адресу:
- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/)

## Дополнительно

### Миграции базы данных
- Генерация миграций:
  ```bash
  poetry run alembic revision --autogenerate -m "Описание изменений"
  ```
- Применение миграций:
  ```bash
  poetry run alembic upgrade head
