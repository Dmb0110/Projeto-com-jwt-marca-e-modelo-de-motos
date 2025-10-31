from fastapi import APIRouter, Request, HTTPException, Depends
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from jose import jwt, JWTError, ExpiredSignatureError
from passlib.context import CryptContext
from models.models import User,Moto
from crud import get_db
from schemas import LoginRequest,MotoOut,CriarMoto,CriarUsuario
from typing import List

# Cria o reteador da API
router = APIRouter()

# Configurações do JWT
SECRET_KEY = "sua_chave_secreta"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Criptografia de senha
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Verifica se a senha fornecida corresponde ao hash
def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)

# Criar um token JWT com tempo de expiração
def create_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# Decofica o token JWT e retorna o usuário
def decode_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload.get("sub")
    except JWTError:
        return None

# Atentica o usuário verificando credenciais
def authenticate_user(db: Session, username: str, password: str):
    user = db.query(User).filter(User.username == username).first()
    if not user or not verify_password(password, user.password):
        return None
    return user

# Verifica se o token JWT é valido e extrai o usuário
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
    try:    # Verifica se o usuário já existe
        usuario_existente = db.query(User).filter(User.username == request.username).first()
        if usuario_existente:
            raise HTTPException(status_code=400, detail="Usuário já existe")

    # Criptografa a senha
        senha_hash = pwd_context.hash(request.password)

    # Cria e salva o novo usuário
        novo_usuario = User(username=request.username, hashed_password=senha_hash)
        db.add(novo_usuario)
        db.commit()
        db.refresh(novo_usuario)
        return {"mensagem": "Usuário registrado com sucesso"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno: {str(e)}")


# Endpoitn para login e geração de token
@router.post("/login")
async def login(request: LoginRequest,db: Session = Depends(get_db)):
    username = request.username
    password = request.password

    user = authenticate_user(db,username,password)
    if not user:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    token = create_token({"sub": username})
    return {"access_token": token}

# Endpoint protegido para criar uma moto
@router.post('/enviar2',response_model=MotoOut)
def enviar(criar: CriarMoto,request: Request,
           db: Session = Depends(get_db),
           usuario: str = Depends(verificar_token)):
    nova_moto = Moto(**criar.dict())
    db.add(nova_moto)
    db.commit()
    db.refresh(nova_moto)
    return nova_moto

# Endpoint protegido para listar motos
@router.get('/receber2',response_model=List[MotoOut])
def receber(
        request: Request,
        db: Session = Depends(get_db),
        usuario: str = Depends(verificar_token)):
    return db.query(Moto).all()

