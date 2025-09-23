
import sys
import os
import pytest
from fastapi.testclient import TestClient
from main import app
#from fastapi import FastAPI

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

#app = FastAPI()
client = TestClient(app)

def test_get():
    response = client.get("/receber6")
    assert response.status_code == 200
    assert response.json() == {"mensagem": "seu teste deu certo,tudo ok por aqui"}

'''
def test_post_item():
    payload = {"name": "Notebook", "price": 2999.90}
    response = client.post("/items", json=payload)
    assert response.status_code == 200
    assert response.json() == payload

'''

#assert "seu teste deu certo" in response.text



