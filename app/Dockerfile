FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN rm -f /app/src/Dockerfile

RUN chmod +x entrypoint.sh

WORKDIR /app/src
ENTRYPOINT ["sh", "/app/entrypoint.sh"]
CMD uvicorn main:app --host 0.0.0.0 --port $APP_PORT
