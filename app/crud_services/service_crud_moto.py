from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from app.models.models_moto import Moto
from app.schemas.schemas import MotoOut, CriarMoto, Atualizar
from typing import List
from app.database.session import get_db, SessionLocal

# Comentário: Você importou FastAPI aqui, mas não está usando.
# Se esse arquivo é apenas de serviço/roteador, pode remover para evitar confusão.

class MotoService:
    # Boa prática: injetar a sessão do banco via Depends(get_db).
    # Isso facilita testes e mantém o código desacoplado.
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def service_criar_moto(self, criar: CriarMoto) -> MotoOut:
        # Uso correto do Pydantic: model_dump para transformar schema em dict.
        nova_moto = Moto(**criar.model_dump())
        self.db.add(nova_moto)
        self.db.commit()
        self.db.refresh(nova_moto)
        # Retorno validado com schema de saída.
        return MotoOut.model_validate(nova_moto)
    
    def service_listar_motos(self) -> List[MotoOut]:
        # Consulta simples e clara.
        motos = self.db.query(Moto).all()
        # Conversão para schema de saída.
        return [MotoOut.model_validate(c) for c in motos]
    
    def service_atualizar_moto(self, id: int, at: Atualizar) -> MotoOut:
        moto = self.db.query(Moto).filter(Moto.id == id).first()
        if not moto:
            # Tratamento de erro com HTTPException.
            raise HTTPException(status_code=404, detail='Moto nao encontrada')
        
        # Atualização manual campo a campo funciona, mas poderia ser mais genérica:
        # usar at.model_dump(exclude_unset=True) para aplicar apenas os campos enviados.
        if at.marca is not None:
            moto.marca = at.marca
        if at.modelo is not None:
            moto.modelo = at.modelo
        
        self.db.commit()
        self.db.refresh(moto)
        # Aqui você retorna o modelo SQLAlchemy direto.
        # Melhor seria retornar MotoOut.model_validate(moto) para manter consistência.
        return moto
    
    def service_deletar_moto(self, id: int) -> dict:
        # Busca a moto pelo ID no banco
        moto = self.db.query(Moto).filter(Moto.id == id).first()
        if not moto:
            # Se não encontrar, lança exceção HTTP 404
            raise HTTPException(status_code=404, detail='Moto nao encontrada')

        # Remove a moto encontrada
        self.db.delete(moto)
        self.db.commit()

        # Retorna mensagem de sucesso em formato JSON
        return {'mensagem': 'Moto deletada com sucesso'}
