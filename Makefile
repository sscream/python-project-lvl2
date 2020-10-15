lint:
	poetry run flake8 gendiff tests

mypy:
	poetry run mypy --ignore-missing-imports gendiff/src/

test:
	poetry run pytest tests

check: lint mypy test

install:
	poetry install

coverage:
	poetry run coverage run --source=gendiff.src -m pytest tests
	poetry run coverage xml