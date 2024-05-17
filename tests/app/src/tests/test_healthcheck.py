def test_health_check(app_client):
    response = app_client.get("/api/v1/healthcheck")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}
