lint:
	poetry run flake8 gendiff tests

mypy:
	poetry run mypy --ignore-missing-imports gendiff/

test:
	poetry run pytest tests -q

check: lint mypy test

install:
	poetry install

coverage:
	poetry run coverage run --source=gendiff -m pytest tests
	poetry run coverage xml