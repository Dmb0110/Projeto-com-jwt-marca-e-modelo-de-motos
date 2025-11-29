from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.schemas.schemas import CriarUsuario
from app.database.session import get_db
from app.crud_services.service_registro import RegistroService

router = APIRouter()

# Endpoint para registrar novo usuário
@router.post(
        "/",
        summary='Registrar novo usuario',
        status_code=201
)
async def registrar_usuario(
    request: CriarUsuario,
    db: Session = Depends(get_db)
):
    return RegistroService.registrar_usuario(request,db)
