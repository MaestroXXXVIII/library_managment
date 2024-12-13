FROM python:3.12.8-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/src:$PYTHONPATH

RUN apt-get update && apt-get install -y curl
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"

WORKDIR /app
COPY poetry.lock pyproject.toml /app/

RUN poetry install --no-root --no-interaction --no-ansi  # Устанавливаем зависимости

COPY . /app

RUN sed -i '1s|^.*$|#!/app/.venv/bin/python|' /app/.venv/bin/alembic
