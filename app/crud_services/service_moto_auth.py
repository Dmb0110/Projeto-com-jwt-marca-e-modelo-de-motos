from app.models.models_moto import Moto
from app.schemas.schemas import CriarMoto, MotoOut
from sqlalchemy.orm import Session

class MotoServiceAuth:

    @staticmethod
    def criar_moto_auth(criar: CriarMoto, db: Session) -> MotoOut:
        # Usa schema Pydantic (CriarMoto) para validar entrada e converte para dict com model_dump.
        nova_moto = Moto(**criar.model_dump())
        db.add(nova_moto)
        db.commit()
        db.refresh(nova_moto)
        # Aqui você retorna o objeto SQLAlchemy direto.
        # Melhor seria retornar MotoOut.model_validate(nova_moto) para manter consistência com o schema de saída.
        return nova_moto
    
    @staticmethod
    def listar_motos_auth(db: Session) -> list[MotoOut]:
        # Consulta todas as motos no banco.
        motos = db.query(Moto).all()
        # Converte cada objeto SQLAlchemy para schema Pydantic de saída.
        return [MotoOut.model_validate(moto) for moto in motos]
