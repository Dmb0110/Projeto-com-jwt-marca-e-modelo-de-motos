import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

'''
pytest -s -v tests/test_postget_auth.py

'''

@pytest.fixture
def token_valido():
    # Registra um usuário
    moto = {"username": "admin15", "password": "1234"}
    client.post("/registro/", json=moto)

    # Faz login e pega o token
    response = client.post("/login/", json=moto)
    data = response.json()
    return data["access_token"]

def test_criar_moto_auth(token_valido):
    nova_moto = {
        "marca": "yamaha",
        "modelo": "xr 180"
    }
    response = client.post(
        "/moto_auth/",  # rota de criação de cliente
        json=nova_moto,
        headers={"Authorization": f"Bearer {token_valido}"}
    )
    assert response.status_code == 200 or response.status_code == 201
    data = response.json()
    assert data["marca"] == "yamaha"
    assert data["modelo"] == "xr 180"
    print('TESTE BEM SUCEDIDO,MOTO CRIADA COM AUTENTICACAO COM SUCESSO')

