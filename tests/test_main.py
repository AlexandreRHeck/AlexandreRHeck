from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)

def test_register_and_login():
    response = client.post('/auth/register', json={'username': 'alice', 'password': 'secret', 'role': 'admin'})
    assert response.status_code == 200
    login_response = client.post('/auth/login', data={'username': 'alice', 'password': 'secret'})
    assert login_response.status_code == 200
    token = login_response.json()['access_token']
    me_response = client.get('/users/me', headers={'Authorization': f'Bearer {token}'})
    assert me_response.status_code == 200
    assert me_response.json()['username'] == 'alice'
