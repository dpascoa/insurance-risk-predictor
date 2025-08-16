import pytest
from app import app
import json

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert json.loads(response.data) == {'status': 'healthy'}

def test_predict_risk_valid(client):
    response = client.post('/predict_risk', data=json.dumps({
        'age': 30,
        'driving_experience_years': 5,
        'vehicle_type': 'van',
        'past_accidents': 1
    }), content_type='application/json')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'risk_score' in data
    assert isinstance(data['risk_score'], float)

def test_predict_risk_invalid(client):
    response = client.post('/predict_risk', data=json.dumps({
        'age': 30
    }), content_type='application/json')
    assert response.status_code == 400
    assert json.loads(response.data) == {'error': 'Missing required fields'}