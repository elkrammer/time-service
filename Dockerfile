# Docker Image for Time Service
FROM python:3.9.1-slim

# Env variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=/app

RUN apt-get update && \
    apt-get install -y --no-install-recommends netcat && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# copy project files
COPY poetry.lock ./
COPY pyproject.toml ./
COPY ./app /app/app

# install project files
RUN pip install poetry==1.0.* && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev

EXPOSE 8000
WORKDIR /app
CMD uvicorn --host=0.0.0.0 app.main:app
