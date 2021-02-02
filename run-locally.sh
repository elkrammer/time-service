#!/usr/bin/env sh

export PYTHONPATH=${PWD}

if ! command -v poetry &> /dev/null
then
    echo "Poetry was not found in the PATH. Please install poetry and make sure you are running Python 3.6+"
    exit
fi

poetry install
poetry run uvicorn app.main:app --reload
