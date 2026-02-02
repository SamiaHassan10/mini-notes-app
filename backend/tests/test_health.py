from backend.app import app


def test_health_endpoint():
    client = app.test_client()
    res = client.get("/")
    assert res.status_code == 200
    assert res.get_json() == {"status": "Backend running"}
