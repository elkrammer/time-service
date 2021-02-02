#!/usr/bin/env sh

export PYTHONPATH=${PWD}

poetry install
poetry run uvicorn app.main:app --reload
