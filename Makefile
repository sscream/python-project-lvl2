lint:
	poetry run flake8 gendiff tests

test:
	poetry run pytest tests

install:
	poetry install

coverage:
	poetry run coverage run --source=gendiff.src -m pytest tests
	poetry run coverage xml