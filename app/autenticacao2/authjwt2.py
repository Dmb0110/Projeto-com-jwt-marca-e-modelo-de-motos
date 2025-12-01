from fastapi import APIRouter, Request, HTTPException, Depends
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from jose import jwt, JWTError, ExpiredSignatureError
from passlib.context import CryptContext
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.models.models_moto import Moto
from app.models.models_user import User
from app.database.session import get_db
from app.schemas.schemas import LoginUsuario,MotoOut,CriarMoto,CriarUsuario
from typing import List
import os

# Bom uso do APIRouter para modularizar rotas. Isso facilita a escalabilidade do projeto.
router = APIRouter()

# SECRET_KEY está sendo buscada via os.getenv, o que é correto, mas seria interessante
# validar se a variável existe e lançar erro caso esteja ausente. Isso evita rodar a aplicação
# sem chave de segurança definida.
SECRET_KEY = os.getenv("SECRET_KEY")

# Algoritmo JWT bem definido e tempo de expiração configurado.
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Uso do passlib com bcrypt é adequado para hashing seguro de senhas.
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Esquema
security = HTTPBearer()


# Seria interessante tipar melhor as funções, por exemplo:
# def verify_password(plain: str, hashed: str) -> bool
def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)

# create_token está bem implementada, mas poderia incluir claims adicionais
# como roles ou permissões para suportar RBAC (Role-Based Access Control).
def create_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# decode_token retorna apenas o "sub". Seria interessante retornar o payload inteiro
# ou valir mais campos (como iat, iss) para maior segurança.
def decode_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload.get("sub")
    except JWTError:
        return None

# authenticate_user está correto, mas poderia lançar exceções específicas
# em vez de retornar None, para facilitar o tratamento de erros.
def authenticate_user(db: Session, username: str, password: str):
    user = db.query(User).filter(User.username == username).first()
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user

# verificar_token trata bem casos de token inválido ou expirado.
# Sugestão: mover lógica de autenticação para um módulo separado (ex: auth_service.py)
# e deixar o router apenas com as rotas. Isso melhora a separação de responsabilidades.
def verificar_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Token inválido")
        return username
    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expirado")
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")
