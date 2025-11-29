from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

   
'''
pytest -s -v tests/test_registro.py

'''

def test_registro_usuario_sucesso():
    novo_usuario = {"username": "admin15", "password": "1234"}
    response = client.post("/registro/", json=novo_usuario)
    assert response.status_code == 201
    data = response.json()
    assert data["mensagem"] == "Usuário registrado com sucesso"

def test_registro_usuario_duplicado():
    # Primeiro registro
    usuario = {"username": "admin15", "password": "1234"}
    client.post("/registro/", json=usuario)

    # Segundo registro com mesmo username deve falhar
    response = client.post("/registro/", json=usuario)
    assert response.status_code == 400
    data = response.json()
    assert data["detail"] == "Usuário já existe"

