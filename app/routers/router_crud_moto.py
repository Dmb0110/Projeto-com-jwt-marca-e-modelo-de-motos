from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.schemas.schemas import CriarMoto, MotoOut, Atualizar, Deletar
from app.database.session import get_db
from app.crud_services.service_crud_moto import MotoService
from typing import List

router = APIRouter()

@router.get(
        '/health/',
        summary='Verifica status da api',
        status_code=status.HTTP_200_OK
)
def health_check():
    # Endpoint simples de health check, útil para monitoramento e integração com ferramentas de observabilidade.
    return {'Status': 'Ola desenvolvedor,tudo ok por aqui'}


@router.post(
        '/',
        summary='Criar uma nova moto',
        response_model=MotoOut,
        status_code=status.HTTP_201_CREATED
)
def criar_moto(criar: CriarMoto, service: MotoService = Depends()):
    # Usa schema Pydantic (CriarMoto) para validar entrada.
    # Injeta MotoService via Depends, mantendo separação de responsabilidades.
    return service.service_criar_moto(criar)


@router.get(
        '/',    
        summary='Listar todas as motos',
        response_model=List[MotoOut],
        status_code=status.HTTP_200_OK
)
def listar_motos(service: MotoService = Depends()):
    # Retorna lista de motos convertidas para schema de saída.
    return service.service_listar_motos()


@router.put(
         '/{id}',
        summary='Trocar dados de uma moto',
        response_model=MotoOut,
        status_code=status.HTTP_200_OK
)
def trocar_dados(id: int, at: Atualizar, service: MotoService = Depends()):
    # Atualiza dados de uma moto pelo ID.
    # Sugestão: se for atualização parcial, usar PATCH em vez de PUT.
    return service.service_atualizar_moto(id, at)


@router.delete(
        '/{id}',
        summary='Deletar uma moto',
        status_code=status.HTTP_200_OK
)
def deletar(id: int, service: MotoService = Depends()):
    # Deleta moto pelo ID e retorna mensagem de sucesso.
    # Sugestão: definir response_model para padronizar saída (ex: {"mensagem": "..."}).
    return service.service_deletar_moto(id)
                                        