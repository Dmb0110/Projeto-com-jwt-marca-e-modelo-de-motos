from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


'''
pytest -s -v tests/test_login.py

'''

def test_login_usuario():
    # Primeiro registra o usuário
    usuario = {"username": "admin15", "password": "1234"}
    client.post("/registro/", json=usuario)

    # Agora faz login (JSON, porque a rota usa LoginUsuario)
    response = client.post("/login/", json=usuario)
    '''
    {
        "username": "admin15",
        "password": "1234"
    })
    '''
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data

    print('TOKEN GERADO:',data['access_token'])


