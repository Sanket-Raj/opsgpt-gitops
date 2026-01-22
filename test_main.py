from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    """Ensure the app can start and expose metrics"""
    response = client.get("/metrics")
    assert response.status_code == 200

def test_prediction_flow():
    """Ensure the model inference endpoint accepts valid JSON"""
    response = client.post(
        "/predict",
        json={"text": "Hello world"}
    )
    assert response.status_code == 200
    assert "generated_text" in response.json()