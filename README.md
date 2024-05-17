# How to start

- Copy `.env.example` to `.env`
- Setup env variables.
- Ensure [Docker](https://docs.docker.com/install/) is installed.
- Ensure [Docker Compose](https://docs.docker.com/compose/install/) is
  installed.
- Ensure [Make](https://www.gnu.org/software/make/) is installed.
- If necessary, in `Makefile` change `COMPOSE_CMD := docker compose`
  to `COMPOSE_CMD := docker-compose`, if you're using Compose tool instead of
  Docker extension
- Run `make start`

# Env variables

| Name               | Description                                                         | Is optional | Default |
|--------------------|---------------------------------------------------------------------|-------------|---------|
| LOG_LEVEL          | Log level. One of ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] | True        | INFO    |
| LOG_BASE_FILENAME  | Base filename (prefix) for log files                                | True        | log     |
| LOG_DIRECTORY      | Directory to store logs. Auto created                               | True        | logs    |
| LOG_ROTATION_VALUE | How much log files to store. One log file == one app run            | True        | 5       |
