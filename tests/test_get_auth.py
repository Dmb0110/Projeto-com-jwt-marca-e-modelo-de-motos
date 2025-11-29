
import pytest
from fastapi.testclient import TestClient
from app.main import app
import json

client = TestClient(app)

'''
pytest -s -v tests/test_get_auth.py

'''

@pytest.fixture
def token_valido():
    # Registra um usuário
    usuario = {"username": "admin15", "password": "1234"}
    client.post("/registro/", json=usuario)
    # Faz login e pega o token
    response = client.post("/login/", json=usuario)
    data = response.json()
    return data["access_token"]


def test_listar_motos(token_valido):
    response = client.get(
        "/moto_auth/",
        headers={"Authorization": f"Bearer {token_valido}"}
    )
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

    # Saída formatada em JSON bonito
    print("\n=== Lista de Motos ===")
    print(json.dumps(data, indent=4, ensure_ascii=False))

    #Mostra marca e modelo de cada moto
    print('=== Motos cadastradas ===')
    for moto in data:
        marca = moto.get('marca')
        modelo = moto.get('modelo')
        print(f'- {marca} {modelo}')
    