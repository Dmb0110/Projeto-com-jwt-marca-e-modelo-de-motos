from fastapi import APIRouter, Depends,HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.schemas import CriarMoto,MotoOut
from app.database.session import get_db
from app.crud_services.service_moto_auth import MotoServiceAuth
from app.autenticacao2.authjwt2 import verificar_token,security
from fastapi.security import HTTPBearer

router = APIRouter()

security = HTTPBearer()

# Endpoint protegido para criar uma moto
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
    return MotoServiceAuth.criar_moto_auth(criar,db)


@router.get(
    '/',
    summary='(Rota protegida) que retorna todos as motos',
    response_model=list[MotoOut],
    status_code=status.HTTP_200_OK
)
def listar_motos(
    db: Session = Depends(get_db),
    usuario: str = Depends(verificar_token)
):
    return MotoServiceAuth.listar_motos_auth(db)