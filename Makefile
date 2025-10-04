gendiff:
	uv run gendiff

.PHONY: lint

lint:
	bash -c 'source .venv/bin/activate && ruff check .'