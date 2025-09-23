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
