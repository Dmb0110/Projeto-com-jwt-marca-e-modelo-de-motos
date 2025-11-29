from app.models.models_moto import Moto
from app.schemas.schemas import CriarMoto, MotoOut
from sqlalchemy.orm import Session

class MotoServiceAuth:

    @staticmethod
    def criar_moto_auth(criar: CriarMoto,db: Session) -> MotoOut:
        nova_moto = Moto(**criar.model_dump())
        db.add(nova_moto)
        db.commit()
        db.refresh(nova_moto)
        return nova_moto
    
    @staticmethod
    def listar_motos_auth(db: Session) -> list[MotoOut]:
        motos = db.query(Moto).all()
        return [MotoOut.model_validate(moto) for moto in motos]
    
    