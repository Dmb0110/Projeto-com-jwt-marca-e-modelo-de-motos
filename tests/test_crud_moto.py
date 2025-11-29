import json
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

'''
COMANDOS PRA TESTAR COM PYTEST
pytest tests/test_crud.py

pytest -s -v tests/test_crud_moto.py

pytest

'''

'''
# Teste POST (criar recurso)
def test_criar_moto():
    nova_moto = {"marca": "honda", "modelo": "xr 500"}
    response = client.post('/moto/', json=nova_moto)
    assert response.status_code == 201
    data = response.json()
    assert data["marca"] == "honda"
    assert data['modelo'] == 'xr 500'
    assert "id" in data
    print('TESTE BEM SUCEDIDO,MOTO CRIADA COM SUCESSO')


# Teste GET (listar recurso)
def test_listar_motos():
    response = client.get("/moto/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0

'''
# Teste GET (listar todos e imprimir todos)
def test_get():
    response = client.get("/moto/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data,list)
    assert len(data) > 0
    #assert response.json()[0]["nome_do_banco"] == "bradesco"
    print('\n [TESTE BEM SUCEDIDO,DADOS RETORNADOS]:')
    print(json.dumps(data,indent=2,ensure_ascii=False))
'''

# Teste PUT (atualizar recurso)
def test_atualizar_moto():
    moto_atualizada = {"marca": "honda", "modelo": "xr 700"}
    response = client.put("/moto/15", json=moto_atualizada)
    assert response.status_code == 200
    data = response.json()
    assert data["marca"] == "honda"
    assert data['modelo'] == 'xr 700'
    print('TESTE BEM SUCEDIDO,MOTO ATUALIZADA COM SUCESSO')


# Teste DELETE (remover recurso)
def test_deletar_moto():
    response = client.delete("/moto/16")
    assert response.status_code == 200
    data = response.json()
    #assert data["mensagem"] == "MOTO DELETADA COM SUCESSO"
    print('TESTE BEM SUCEDIDO,MOTO DELETADA COM SUCESSO')
'''

