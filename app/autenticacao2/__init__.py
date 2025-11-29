'''

from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from models import User
from crud import get_db

# 🔐 Chave secreta usada para assinar e verificar os tokens JWT
SECRET_KEY = "sua_chave_secreta"
# 🔐 Algoritmo de assinatura usado para gerar o JWT (HMAC com SHA-256)
ALGORITHM = "HS256"
# ⏱️ Tempo de expiração do token de acesso (em minutos)
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# 🔒 Configuração do contexto de criptografia de senhas usando bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# 🛡️ Define o esquema de autenticação OAuth2 para extrair o token JWT do header Authorization
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
####################################################
###################################################

# 🔍 Verifica se a senha digitada corresponde ao hash armazenado
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# 🔐 Gera um hash seguro da senha para armazenar no banco de dados
def get_password_hash(password):
    return pwd_context.hash(password)

# 🔎 Autentica o usuário verificando se o nome de usuário existe e se a senha está correta
def authenticate_user(db: Session, username: str, password: str):
    # Busca o usuário no banco de dados pelo nome de usuário
    user = db.query(User).filter(User.username == username).first()
    # Se o usuário não existir ou a senha estiver incorreta, retorna None
    if not user or not verify_password(password, user.password):
        return None
    # Se tudo estiver certo, retorna o objeto do usuário
    return user

# 🧪 Cria um token JWT com os dados fornecidos e tempo de expiração
def create_access_token(data: dict, expires_delta: timedelta = None):
    # Copia os dados para evitar modificar o original
    to_encode = data.copy()
    # Define o tempo de expiração do token
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    # Adiciona a expiração ao payload do token
    to_encode.update({"exp": expire})
    # Gera e retorna o token JWT assinado com a chave secreta e algoritmo definido
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# 🔐 Recupera o usuário atual a partir do token JWT enviado na requisição
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    # Define uma exceção padrão para falhas de autenticação
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token inválido",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        # Decodifica o token JWT usando a chave secreta e algoritmo
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        # Extrai o nome de usuário do payload (campo "sub")
        username = payload.get("sub")
        # Se não houver nome de usuário, lança exceção
        if username is None:
            raise credentials_exception
    except JWTError:
        # Se houver erro na decodificação do token, lança exceção
        raise credentials_exception
    # Busca o usuário no banco de dados
    user = db.query(User).filter(User.username == username).first()
    # Se o usuário não existir, lança exceção
    if user is None:
        raise credentials_exception
    # Retorna o usuário autenticado
    return user



SECRET_KEY = 'minha_senha_secreta'

ALGORITHM = 'HS256'

ACCESS_TOKEN_EXPIRE_MINUTES = 90

pwd_context =

def verify_password(plain_password,hash_password):
    return pwd_context.verify(plain_password,hash_password)

def get_verify_password(password):
    return pwd_context.hash(password)

def autenticate_user(db: Session,username: str,password: str):
    info = db.query(User).filter(User.username == username).first()
    if not info or verifyy_password(password,info.password)
        return None
    return info

'''