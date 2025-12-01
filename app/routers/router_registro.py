from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.schemas import CriarUsuario
from app.database.session import get_db
from app.crud_services.service_registro import RegistroService

router = APIRouter()

@router.post(
        "/",
        summary='Registrar novo usuário',
        status_code=201
)
async def registrar_usuario(
    request: CriarUsuario,
    db: Session = Depends(get_db)
):
    # Usa schema Pydantic (CriarUsuario) para validar entrada.
    # Injeta a sessão do banco via Depends(get_db).
    # Delegação da lógica para RegistroService mantém separação de responsabilidades.
    return RegistroService.registrar_usuario(request, db)
