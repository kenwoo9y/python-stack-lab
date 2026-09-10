include .env
export

.PHONY: help build-local up down logs ps migrate psql test test-coverage lint-check lint-fix format-check format-fix
.DEFAULT_GOAL := help

build-local: ## Build docker image to local development
	docker compose build --no-cache

up: ## Do docker compose up
	docker compose up

down: ## Do docker compose down
	docker compose down

logs: ## Tail docker compose logs
	docker compose logs -f

ps: ## Check container status
	docker compose ps

migrate:  ## Execute migration
	docker-compose run --rm --entrypoint bash todo-api -c "uv sync && uv run python -m api.migrate_db"

psql: ## Access PostgreSQL Database
	docker compose exec postgresql-db psql -U $$DB_USER -d $$DB_NAME -W

test: ## Execute tests
	docker-compose run --entrypoint "uv run pytest -v" todo-api

test-coverage: ## Execute tests with coverage
	docker-compose run --entrypoint "uv run pytest --cov" todo-api

lint-check: ## Run Ruff linter
	uv run ruff check .

lint-fix: ## Run Ruff linter and apply fixes
	uv run ruff check . --fix

format-check: ## Check code formatting with Ruff
	uv run ruff format . --check --diff

format-fix: ## Format code with Ruff
	uv run ruff format .

help: ## Show options
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' Makefile | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'