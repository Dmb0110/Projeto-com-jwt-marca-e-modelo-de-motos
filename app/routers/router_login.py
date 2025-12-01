from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.schemas import LoginUsuario
from app.database.session import get_db
from app.crud_services.service_login import LoginService

router = APIRouter()

@router.post(
        "/",
        summary='Criar Login para o usuário e gerar o token',
        status_code=200
)
async def login(request: LoginUsuario, db: Session = Depends(get_db)):
    # Usa schema Pydantic (LoginUsuario) para validar entrada (username e password).
    # Injeta a sessão do banco via Depends(get_db).
    # Delegação da lógica para LoginService mantém separação de responsabilidades.
    return LoginService.login(request, db)
