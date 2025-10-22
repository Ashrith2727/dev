from app import app

def test_index():
    c = app.test_client()
    rv = c.get('/')
    assert rv.status_code == 200
    assert b"Hello" in rv.data

def test_health():
    c = app.test_client()
    rv = c.get('/health')
    assert rv.get_json() == {"status": "ok"}
