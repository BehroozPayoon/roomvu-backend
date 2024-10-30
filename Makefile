ifneq ($(wildcard docker/.env.example),)
    ENV_FILE = .env.example
endif
ifneq ($(wildcard .env.example),)
	ifeq ($(COMPOSE_PROJECT_NAME),)
    	include .env.example
	endif
endif
ifneq ($(wildcard docker/.env),)
    ENV_FILE = .env
endif
ifneq ($(wildcard .env),)
	ifeq ($(COMPOSE_PROJECT_NAME),)
		include .env
	endif
endif

docker_compose = docker compose -f docker/docker-compose.yml --env-file docker/$(ENV_FILE)

export

.PHONY: run-api
run-api: ## Run backend
	poetry run gunicorn --reload --bind $(HOST):$(BACKEND_PORT) \
	--worker-class uvicorn.workers.UvicornWorker \
	--workers $(API_WORKERS) --log-level $(LEVEL) --chdir cmd/api main:app

.PHONY: develop-api
develop-api: ## Hot reload backend
	poetry run uvicorn src.server:app --reload --host 0.0.0.0 --port 8080 --log-level debug

.PHONY: compose-up
compose-up: ## Create and start containers
	$(docker_compose) up -d

.PHONY: compose-down
compose-down: ## Create and start containers
	$(docker_compose) down