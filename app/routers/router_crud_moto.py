from fastapi import APIRouter,Depends,status
from sqlalchemy.orm import Session
from app.schemas.schemas import CriarMoto,MotoOut,Atualizar,Deletar
from app.database.session import get_db
from app.crud_services.service_crud_moto import MotoService
from typing import List
#from starlette.status import HTTP_201_CREATED as status_HTTP_201_OK

router = APIRouter()

# Endpoint para criar uma nova moto
@router.post(
        '/',
        summary='Criar uma nova moto',
        response_model=MotoOut,
        status_code=status.HTTP_201_CREATED
)
def criar_moto(criar: CriarMoto,service: MotoService = Depends()):
    return service.service_criar_moto(criar)


@router.get(
    '/',
    summary='Listar todas as motos',
    response_model=List[MotoOut],
    status_code=status.HTTP_200_OK
)
def listar_motos(service: MotoService = Depends()):
    return service.service_listar_motos()


@router.put(
    '/{id}',
    summary='Trocar dados de uma moto',
    response_model=MotoOut,
    status_code=status.HTTP_200_OK
)
def trocar_dados(id: int,at: Atualizar,service: MotoService = Depends()):
    return service.service_atualizar_moto(id,at)


@router.delete(
    '/{id}',
    summary='Deletar uma moto',
    status_code=status.HTTP_200_OK
)
def deletar(id: int,service: MotoService = Depends()):
    return service.service_deletar_moto(id)
