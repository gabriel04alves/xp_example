from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_login_returns_token():
    response = client.post("/token")
    assert response.status_code == 200
    assert "access_token" in response.json