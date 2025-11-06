from typing import Optional
from pydantic import BaseModel,constr,ConfigDict

# Modelo para criação de usuário
class CriarUsuario(BaseModel):
    password: constr(max_length=72)
    password: constr(min_length=2, max_length=72)

# Modelo para requisição de login
class LoginRequest(BaseModel):
    username: contr(max_length=72)
    password: constr(min_length=2, max_length=72)
#############################################################
# Modelo para criação de moto
class CriarMoto(BaseModel):
    marca: str
    modelo: str

# Modelo de saída da moto (inclui ID)
class MotoOut(BaseModel):
    id: int
    marca: str
    modelo: str

    # Permite criar o modelo a partir de atributos ORM
    model_config = ConfigDict(
        from_attributes=True
    )

# Modelo para atualização parcial da moto
class Atualizar(BaseModel):
    marca: Optional[str] = None
    modelo: Optional[str] = None

# Modelo para resposta de exclusão
class Deletar(BaseModel):
    mensagem: bool








































'''
from fastapi import APIRouter, Request, HTTPException, Depends
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from jose import jwt, JWTError, ExpiredSignatureError
from passlib.context import CryptContext
from models.models import User, Moto
from crud import get_db
from schemas import LoginRequest, MotoOut, CriarMoto, CriarUsuario
from typing import List
import os

# Cria o roteador da API
router = APIRouter()

# Configurações do JWT
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Criptografia de senha
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# 🔐 Truncamento seguro por bytes
def truncate_password(password: str) -> str:
    password_bytes = password.encode("utf-8")[:72]
    return password_bytes.decode("utf-8", errors="ignore")

# Verifica se a senha fornecida corresponde ao hash
def verify_password(plain: str, hashed: str) -> bool:
    plain_truncada = truncate_password(plain)
    return pwd_context.verify(plain_truncada, hashed)

# Cria um token JWT com tempo de expiração
def create_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# Decodifica o token JWT e retorna o usuário
def decode_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload.get("sub")
    except JWTError:
        return None

# Autentica o usuário verificando credenciais
def authenticate_user(db: Session, username: str, password: str):
    user = db.query(User).filter(User.username == username).first()
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user

# Verifica se o token JWT é válido e extrai o usuário
def verificar_token(request: Request):
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Token ausente ou mal formatado")

    token = auth_header.split(" ")[1]
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

# Endpoint para registrar novo usuário
@router.post("/registro", status_code=201)
def registrar_usuario(request: CriarUsuario, db: Session = Depends(get_db)):
    try:
        usuario_existente = db.query(User).filter(User.username == request.username).first()
        if usuario_existente:
            raise HTTPException(status_code=400, detail="Usuário já existe")

        senha_truncada = truncate_password(request.password)
        senha_hash = pwd_context.hash(senha_truncada)

        novo_usuario = User(username=request.username, hashed_password=senha_hash)
        db.add(novo_usuario)
        db.commit()
        db.refresh(novo_usuario)
        return {"mensagem": "Usuário registrado com sucesso"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno: {str(e)}")

# Endpoint para login e geração de token
@router.post("/login")
async def login(request: LoginRequest, db: Session = Depends(get_db)):
    username = request.username
    password = request.password

    user = authenticate_user(db, username, password)
    if not user:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    token = create_token({"sub": username})
    return {"access_token": token}

# Endpoint protegido para criar uma moto
@router.post('/enviar2', response_model=MotoOut)
def enviar(criar: CriarMoto, request: Request,
           db: Session = Depends(get_db),
           usuario: str = Depends(verificar_token)):
    nova_moto = Moto(**criar.dict())
    db.add(nova_moto)
    db.commit()
    db.refresh(nova_moto)
    return nova_moto

# Endpoint protegido para listar motos
@router.get('/receber2', response_model=List[MotoOut])
def receber(request: Request,
            db: Session = Depends(get_db),
            usuario: str = Depends(verificar_token)):
    return db.query(Moto).all()
'''
    
