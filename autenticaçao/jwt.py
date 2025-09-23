'''from datetime import datetime, timedelta
from jose import JWTError, jwt

SEGREDO = "sua-chave-secreta"
ALGORITMO = "HS256"
EXPIRA_MINUTOS = 30

def criar_token(dados: dict) -> str:
    dados_para_token = dados.copy()
    expiracao = datetime.utcnow() + timedelta(minutes=EXPIRA_MINUTOS)
    dados_para_token.update({"exp": expiracao})
    return jwt.encode(dados_para_token, SEGREDO, algorithm=ALGORITMO)

def verificar_token(token: str) -> dict:
    try:
        dados = jwt.decode(token, SEGREDO, algorithms=[ALGORITMO])
        return dados
    except JWTError:
        return None

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from autenticacao.jwt import verificar_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

def usuario_autenticado(token: str = Depends(oauth2_scheme)):
    dados = verificar_token(token)
    if not dados:
        raise HTTPException(status_code=401, detail="Token inválido ou expirado")
    return dados


from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from autenticacao.jwt import criar_token
from autenticacao.seguranca import verificar_senha
from modelos import Usuario  # Supondo que você tenha um modelo de usuário
from banco_de_dados import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.email == form_data.username).first()
    if not usuario or not verificar_senha(form_data.password, usuario.senha_hash):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    token = criar_token({"sub": usuario.email})
    return {"access_token": token, "token_type": "bearer"}

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def gerar_hash_senha(senha: str) -> str:
    return pwd_context.hash(senha)

def verificar_senha(senha: str, hash: str) -> bool:
    return pwd_context.verify(senha, hash)


# app.py

# 📦 Imports
from datetime import datetime, timedelta
from fastapi import FastAPI, APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from schemas import Atualizar, AlunoOut, CriarAluno,Deletar
from models import Aluno
from ..schemas import Atualizar,AlunoOut,CriarAluno,Deletar

# 🛠️ Configurações do JWT
SEGREDO = "sua-chave-secreta"
ALGORITMO = "HS256"
EXPIRA_MINUTOS = 30

# 🔐 Funções de Autenticação JWT
def criar_token(dados: dict) -> str:
    dados_para_token = dados.copy()
    expiracao = datetime.utcnow() + timedelta(minutes=EXPIRA_MINUTOS)
    dados_para_token.update({"exp": expiracao})
    return jwt.encode(dados_para_token, SEGREDO, algorithm=ALGORITMO)

def verificar_token(token: str) -> dict | None:
    try:
        return jwt.decode(token, SEGREDO, algorithms=[ALGORITMO])
    except JWTError:
        return None

# 🔒 Segurança de Senhas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def gerar_hash_senha(senha: str) -> str:
    return pwd_context.hash(senha)

def verificar_senha(senha: str, hash: str) -> bool:
    return pwd_context.verify(senha, hash)

# 🔑 Dependência de Autenticação
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

def usuario_autenticado(token: str = Depends(oauth2_scheme)):
    dados = verificar_token(token)
    if not dados:
        raise HTTPException(status_code=401, detail="Token inválido ou expirado")
    return dados

# 🧩 Simulação de banco de dados e modelo de usuário
# Substitua com suas implementações reais
class Usuario:
    def __init__(self, email: str, senha_hash: str):
        self.email = email
        self.senha_hash = senha_hash

# Simulação de banco de dados
def get_db():
    class FakeDB:
        def query(self, modelo):
            class Query:
                def filter(self, condicao):
                    # Simulação: retorna um usuário com senha "1234"
                    return [Usuario(email="teste@exemplo.com", senha_hash=gerar_hash_senha("1234"))]
            return Query()
    return FakeDB()

# 🚪 Rota de Login
router = APIRouter()

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.email == form_data.username)[0]
    if not usuario or not verificar_senha(form_data.password, usuario.senha_hash):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    token = criar_token({"sub": usuario.email})
    return {"access_token": token, "token_type": "bearer"}

@router.get("/perfil")
def perfil(usuario: dict = Depends(usuario_autenticado)):
    return {"mensagem": f"Bem-vindo, {usuario['sub']}!"}

@router.post("/enviar", response_model=AlunoOut)
def enviar(
    criar: CriarAluno,
    db: Session = Depends(get_db),
    usuario: dict = Depends(usuario_autenticado)  # 👈 Proteção aqui
):
    novo = Aluno(**criar.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo



# 🚀 Inicialização do FastAPI
app = FastAPI()
app.include_router(router)

#rota para cadastrar usuario e senha pra acessar os endpoints da fastapi
@router.post("/cadastro")
def cadastrar_usuario(
    novo_usuario: CriarUsuario,  # modelo Pydantic com email e senha
    db: Session = Depends(get_db)
):
    # Verifica se o usuário já existe
    existente = db.query(Usuario).filter(Usuario.email == novo_usuario.email).first()
    if existente:
        raise HTTPException(status_code=400, detail="Usuário já cadastrado")

    # Cria novo usuário com senha criptografada
    senha_hash = gerar_hash_senha(novo_usuario.senha)
    usuario = Usuario(email=novo_usuario.email, senha_hash=senha_hash)
    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    return {"mensagem": "Usuário cadastrado com sucesso"}




# modelo pydantic para o endpoint cadastro
from pydantic import BaseModel, EmailStr

class CriarUsuario(BaseModel):
    email: EmailStr
    senha: str

# codigo requests para o modelo pydantic criarusuario
import requests

url = "http://localhost:8000/cadastro"
payload = {
    "email": "teste@exemplo.com",
    "senha": "1234"
}

response = requests.post(url, json=payload)
print(response.json())



import requests

url = 'http://127.0.0.1:8000/receber'

dados = {
    'marca': 'honda',
    'modelo': 'cb 500'
}

dados = {
    'nome': 'dj',
    'idade': 34
}

resposta = requests.get(url,json=dados)

resposta = requests.get(url)

print(resposta.status_code)
print(resposta.json())


import requests

token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0ZTUiLCJleHAiOjE3NTQ4Njk1ODN9.6gJIcfcQni8XQSO2LkYl0nvbU5pKy2k3vsgeaxq63iY'

url = 'http://127.0.0.1:8000/enviar2'

cabecalhos = {
    'Authorization': f'Bearer {token}'
}

dados = {
    'marca': 'yamaha',
    'modelo': 'xr 100'
}

resposta = requests.post(url,json=dados,headers=cabecalhos)

print('Código de status:', resposta.status_code)

try:
    print('Resposta da API:', resposta.json())
except ValueError:
    print('Resposta da API (texto):', resposta.text)

#####################################################
import requests

token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0ZTUiLCJleHAiOjE3NTQ5MzQ3NTR9.Wi5UBZRrOFMZJN3x2JkAXKVykKearEpii11565hkL2s'

url = 'http://127.0.0.1:8000/trocar3/4'

moto_id = 4

dados = {
    'marca':'yamaha',
    'modelo':'mt-80'
}

headers = {
    'Authorization': f'Bearer {token}',
    'Content_Type': 'application/json'
}

resposta = requests.put(url,json=dados,headers=headers)

print('status:',resposta.status_code)
try:
    print('resposta:',resposta.json())
except ValueError:
    print('resposta:',resposta.text)
'''
###########################################################
import requests

url = 'http://127.0.0.1:8000/trocar1/1'

info = {
    'marca':'yamaha',
    'modelo':'mt-200'
}

resposta = requests.put(url,json=info)

print(resposta.status_code)
print(resposta.json())



