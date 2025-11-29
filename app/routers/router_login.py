from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.schemas.schemas import LoginUsuario
from app.database.session import get_db
from app.crud_services.service_login import LoginService

router = APIRouter()

# Endpoitn para login e geração de token
@router.post(
        "/",
        summary='Criar Login para o usuaro e gera o token',
        status_code=200
)
async def login(request: LoginUsuario,db: Session = Depends(get_db)):
    return LoginService.login(request,db)

