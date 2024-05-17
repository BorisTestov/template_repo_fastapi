FROM python:3.12-slim


WORKDIR /

COPY tests tests
RUN pip install --no-cache-dir -r tests/requirements.txt

COPY app app
RUN pip install --no-cache-dir -r app/requirements.txt

CMD python /tests/run_tests.py
