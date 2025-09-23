from fastapi import HTTPException
from fastapi import FastAPI
from models import Base, engine
from crud import router as crud_router
from autenticacao2.authjwt2 import router as auth_router
#from test_crud import router

#  Cria instancia da aplicaçao FastAPI
app = FastAPI()

#  Cria tabelas no banco de dados
Base.metadata.create_all(bind=engine)

#  Incluir rotas publicas e privadas na aplicaçao
app.include_router(auth_router)
app.include_router(crud_router)
#app.include_router(router)

@app.get('/receber6')
def resposta():
    return {'mensagem':'ola mundo'}


'''
enviar
receber
jwt

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth_router)
app.include_router(auth_router)


app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth_router)
app.include_router(crud_router)




@router.post("/enviar2")
def enviar(criar: CriarMoto, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    try:
        nova_moto = Moto(**criar.dict(), dono_id=current_user.id)
        db.add(nova_moto)
        db.commit()
        db.refresh(nova_moto)
        return nova_moto
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno: {str(e)}")

from fastapi import FastAPI

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth_router)
app.include_router(crud_router)

from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta

# 🔧 Configurações do JWT
SEGREDO = "sua-chave-secreta"
ALGORITMO = "HS256"
EXPIRA_MINUTOS = 30

# 🔐 Segurança de senha
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# 🔑 OAuth2 esquema
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

# 🚀 Inicialização do FastAPI
app = FastAPI()

# 🧠 Simulação de usuário em memória
usuarios_fake = {
    "teste@exemplo.com": {
        "email": "teste@exemplo.com",
        "senha_hash": pwd_context.hash("1234")
    }
}

# 🔐 Funções JWT
def criar_token(dados: dict) -> str:
    dados_para_token = dados.copy()
    expiracao = datetime.utcnow() + timedelta(minutes=EXPIRA_MINUTOS)
    dados_para_token.update({"exp": expiracao})
    return jwt.encode(dados_para_token, SEGREDO, algorithm=ALGORITMO)

def verificar_token(token: str) -> dict:
    try:
        return jwt.decode(token, SEGREDO, algorithms=[ALGORITMO])
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido ou expirado")

def usuario_autenticado(token: str = Depends(oauth2_scheme)):
    return verificar_token(token)

# 🔐 Verificação de senha
def verificar_senha(senha: str, hash: str) -> bool:
    return pwd_context.verify(senha, hash)

# 🚪 Rota de login
@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    usuario = usuarios_fake.get(form_data.username)
    if not usuario or not verificar_senha(form_data.password, usuario["senha_hash"]):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    token = criar_token({"sub": usuario["email"]})
    return {"access_token": token, "token_type": "bearer"}

# 🔒 Rota protegida
@app.get("/perfil")
def perfil(usuario: dict = Depends(usuario_autenticado)):
    return {"mensagem": f"Bem-vindo, {usuario['sub']}!"}





app = FastAPI()

Base.metadata.crate_all(bind=engine)

app.include_router(router)

#####################################################################

from fastapi import FastAPI
from models import Base, engine
from crud import router as crud_router
from auth import router as auth_router  # rotas de login/registro

app = FastAPI()

# Cria as tabelas no banco
Base.metadata.create_all(bind=engine)

# Inclui as rotas da API principal
app.include_router(crud_router)

# Inclui as rotas de autenticação JWT
app.include_router(auth_router, prefix="/auth", tags=["Autenticação"])


from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from passlib.context import CryptContext
from jose import JWTError, jwt
from typing import List, Optional
from datetime import datetime, timedelta

# ==================== CONFIGURAÇÕES ====================
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

DATABASE_URL = "postgresql://postgres:davi9090@localhost:5432/banco_dmb"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

SECRET_KEY = "minha_chave_secreta"
ALGORITHM = "HS256"
EXPIRACAO_MINUTOS = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

# ==================== MODELOS ====================
class Usuario(Base):
    __tablename__ = 'usuario5'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True, index=True)
    idade = Column(Integer)
    senha_hash = Column(String)

Base.metadata.create_all(bind=engine)

# ==================== SCHEMAS ====================
class CriarUsuario(BaseModel):
    nome: str
    idade: int
    senha: str

class UsuarioOut(BaseModel):
    id: int
    nome: str
    idade: int

    class Config:
        orm_mode = True

class Atualizar(BaseModel):
    nome: Optional[str] = None
    idade: Optional[int] = None

class Deletar(BaseModel):
    mensagem: bool

class Token(BaseModel):
    access_token: str
    token_type: str

# ==================== FUNÇÕES JWT ====================
def gerar_hash_senha(senha: str):
    return pwd_context.hash(senha)

def verificar_senha(senha_plana, senha_hash):
    return pwd_context.verify(senha_plana, senha_hash)

def criar_token(dados: dict):
    dados_para_codificar = dados.copy()
    expiracao = datetime.utcnow() + timedelta(minutes=EXPIRACAO_MINUTOS)
    dados_para_codificar.update({"exp": expiracao})
    return jwt.encode(dados_para_codificar, SECRET_KEY, algorithm=ALGORITHM)

def verificar_token(token: str):
    try:
        carga = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return carga.get("sub")
    except JWTError:
        return None

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    username = verificar_token(token)
    if not username:
        raise HTTPException(status_code=401, detail="Token inválido ou expirado")
    usuario = db.query(Usuario).filter(Usuario.nome == username).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return usuario

# ==================== ROTAS ====================
@app.post('/registrar')
def registrar(usuario: CriarUsuario, db: Session = Depends(get_db)):
    senha_segura = gerar_hash_senha(usuario.senha)
    novo = Usuario(nome=usuario.nome, idade=usuario.idade, senha_hash=senha_segura)
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return {"mensagem": "Usuário registrado com sucesso"}

@app.post('/login', response_model=Token)
def login(form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.nome == form.username).first()
    if not usuario or not verificar_senha(form.password, usuario.senha_hash):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    token = criar_token({"sub": usuario.nome})
    return {"access_token": token, "token_type": "bearer"}

@app.post('/dados', response_model=UsuarioOut)
def criar_usuario(usuario: CriarUsuario, db: Session = Depends(get_db), user=Depends(get_current_user)):
    novo = Usuario(nome=usuario.nome, idade=usuario.idade, senha_hash=gerar_hash_senha(usuario.senha))
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

@app.get('/dados', response_model=List[UsuarioOut])
def exibir(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return db.query(Usuario).all()

@app.put('/dados/{id}')
def trocar(id: int, atualizar: Atualizar, db: Session = Depends(get_db), user=Depends(get_current_user)):
    dados = db.query(Usuario).filter(Usuario.id == id).first()
    if not dados:
        return {'Erro': 'usuario nao encontrado'}
    if atualizar.nome is not None:
        dados.nome = atualizar.nome
    if atualizar.idade is not None:
        dados.idade = atualizar.idade
    db.commit()
    return {'mensagem': 'dados atualizados com sucesso'}

@app.delete('/dados/{id}')
def deletar(id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    dados = db.query(Usuario).filter(Usuario.id == id).first()
    if not dados:
        return {'Erro': 'usuario nao encontrado'}
    db.delete(dados)
    db.commit()
    return {'mensagem': 'usuario deletado com sucesso'}

@app.get('/dados/{id}', response_model=UsuarioOut)
def dado_especifico(id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    dados1 = db.query(Usuario).filter(Usuario.id == id).first()
    if not dados1:
        raise HTTPException(status_code=404, detail='usuario nao encontrado')
    return dados1

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router)


'''


