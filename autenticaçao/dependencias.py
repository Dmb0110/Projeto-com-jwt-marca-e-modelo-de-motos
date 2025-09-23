from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from autenticacao.jwt import verificar_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

def usuario_autenticado(token: str = Depends(oauth2_scheme)):
    dados = verificar_token(token)
    if not dados:
        raise HTTPException(status_code=401, detail="Token inválido ou expirado")
    return dados
