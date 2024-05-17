.PHONY: start status logs stop restart tests

COMPOSE_CMD := docker compose

args:
	@$(eval ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS)))

start: args
	@$(COMPOSE_CMD) up -d $(ARGS)

status:
	@$(COMPOSE_CMD) ps -a

logs: args
	@$(COMPOSE_CMD) logs $(ARGS)

stop: args
	@$(COMPOSE_CMD) down $(ARGS)

restart: args
	@$(COMPOSE_CMD) restart $(ARGS)

tests: args
	@$(COMPOSE_CMD) --profile tests up -d --no-deps $(ARGS)

%:
	@: