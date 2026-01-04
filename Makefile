.PHONY: gendiff lint lint-fix test test-coverage

gendiff:
	uv run gendiff

lint:
	bash -c 'source .venv/bin/activate && ruff check .'

lint-fix:
	bash -c 'source .venv/bin/activate && black . && isort .'

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report=xml:coverage.xml