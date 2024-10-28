#!/usr/bin/env just --justfile
set dotenv-load

test:
    uv run python manage.py test --settings=tests.example.settings

lint:
    uvx ruff check

format:
    uvx ruff format

test_publish:
    uv publish --publish-url https://test.pypi.org/legacy/ --token $TEST_PYPI_TOKEN
