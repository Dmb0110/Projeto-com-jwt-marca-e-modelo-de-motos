from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.schemas import CriarMoto, MotoOut
from app.database.session import get_db
from app.crud_services.service_moto_auth import MotoServiceAuth
from app.autenticacao2.authjwt2 import verificar_token, security
from fastapi.security import HTTPBearer

router = APIRouter()

# Você está instanciando security = HTTPBearer(), mas não está usando diretamente.
# Como já injeta verificar_token, pode remover ou usar security como dependência explícita.
security = HTTPBearer()

@router.post(
    '/',
    summary='Criar moto (rota protegida)',
    response_model=MotoOut,
    status_code=status.HTTP_201_CREATED
)
def enviar(
    criar: CriarMoto,
    db: Session = Depends(get_db),
    usuario: str = Depends(verificar_token)
):
    # Protege rota exigindo token válido):
    # Cria moto usando serviço autenticado
    return MotoServiceAuth.criar_moto_auth(criar, db)

@router.get(
    '/',
    summary='(Rota protegida) que retorna todas as motos',
    response_model=list[MotoOut],
    status_code=status.HTTP_200_OK
)
def listar_motos(
    db: Session = Depends(get_db),
    usuario: str = Depends(verificar_token)  # Protege rota exigindo token válido
):
    # Lista motos usando serviço autenticado
    return MotoServiceAuth.listar_motos_auth(db)
