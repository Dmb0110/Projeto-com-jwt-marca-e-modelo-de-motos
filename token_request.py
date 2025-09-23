'''
import requests

url = "http://127.0.0.1:8000/register"  # Altere para o endereço real da sua API

payload = {
    "username": "teste1",
    "password": "1234"
}

response = requests.post(url, json=payload)

if response.status_code == 200:
    token_data = response.json()
    print("Token de acesso:", token_data["access_token"])
else:
    print("Erro:", response.status_code, response.text)


'''
import requests

url = "http://127.0.0.1:8000/login"  # Altere para o endereço real da sua API

payload = {
    "username": "teste1",
    "password": "1234"
}

response = requests.post(url, json=payload)

if response.status_code == 200:
    token_data = response.json()
    print("Token de acesso:", token_data["access_token"])
else:
    print("Erro:", response.status_code, response.text)

'''
"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0ZTEiLCJleHAiOjE3NTcxMDY5NjB9.xaMZPILnYBThkaMFXXXTtsHw-mRgSjAkalVEhjlORBI"

eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0ZTEiLCJleHAiOjE3NTcxMDc4OTd9.xSxZgltfZ43RgvwC3MWrkT7ApuhED9bvoZ_pOAF95rI





'''



