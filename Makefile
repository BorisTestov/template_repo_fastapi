.PHONY: start

COMPOSE_CMD := docker compose

start:
	@$(COMPOSE_CMD) up -d

status:
	@$(COMPOSE_CMD) ps -a

logs:
	@$(COMPOSE_CMD) logs

stop:
	@$(COMPOSE_CMD) down
