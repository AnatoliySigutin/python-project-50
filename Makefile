gendiff:
	uv run gendiff

.PHONY: lint

lint:
	bash -c 'source .venv/bin/activate && ruff check .'

lint-fix:
	bash -c 'source .venv/bin/activate && black . && isort .'