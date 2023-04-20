.DEFAULT_GOAL := help

PROJECT_NAME := BOOK'S CRUD

.PHONY: help
help: 
	@echo "------------------------------------------------------------------------"
	@echo "${PROJECT_NAME}"
	@echo "------------------------------------------------------------------------"
	@grep -E '^[a-zA-Z0-9_/%\-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: db-up
db-up: ## Start DB container
	@docker compose up db --build -d

.PHONY: db-down
db-down: ## Stop DB container
	@docker compose stop db

.PHONY: db-shell ## Open DB shell
db-shell:
	@psql postgres://user:password\@localhost:5432/books-crud\?sslmode=disable

.PHONY: pylint
lint: ## Run pylint
	@pylint *.py

.PHONY: test
test: db-up ## Run interation tests
	@pytest -v -s *.py

.PHONY: run
run: db-up ## Start DB container and run API
	@uvicorn api:app --reload
	@db-down

.PHONY: stop
stop: ## Stop DB container
	@docker compose stop db


