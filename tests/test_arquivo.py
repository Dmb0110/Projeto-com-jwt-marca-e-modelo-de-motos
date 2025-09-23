from fastapi.testclient import TestClient
from crud import app  # substitua 'seu_arquivo' pelo nome do arquivo onde está o app

client = TestClient(app)

def test_get():
    response = client.get("/receber1")
    assert response.status_code == 200
