from fastapi import HTTPException
from fastapi import FastAPI
from models.models import Base, engine
from crud import router as crud_router
from autenticacao2.authjwt2 import router as auth_router
#from test_crud import router
import time

#  Cria instancia da aplicaçao FastAPI
app = FastAPI()


@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine)

#  Cria tabelas no banco de dados
#Base.metadata.create_all(bind=engine)

#  Incluir rotas publicas e privadas na aplicaçao
app.include_router(auth_router)
app.include_router(crud_router)


'''

# Endpoint para registrar novo usuário
@router.post("/registro", status_code=201)
async def registrar_usuario(request: CriarUsuario, db: Session = Depends(get_db)):
    #try:    # Verifica se o usuário já existe
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

    #except Exception as e:
     #   raise HTTPException(status_code=500, detail=f"Erro interno: {str(e)}")




'''

