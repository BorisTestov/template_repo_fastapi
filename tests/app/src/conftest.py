import pytest
from fastapi.testclient import TestClient
from main import app


@pytest.fixture(scope="session")
def app_client():
    client = TestClient(app)
    yield client
    client.close()
