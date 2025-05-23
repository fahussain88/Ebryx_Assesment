from app import app

def test_healthz():
    client = app.test_client()
    response = client.get('/healthz')
    assert response.status_code == 200

def test_failcheck():
    client = app.test_client()
    response = client.get('/failcheck')
    assert response.status_code == 500