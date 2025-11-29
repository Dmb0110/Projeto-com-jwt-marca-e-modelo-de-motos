from fastapi import APIRouter, HTTPException, Depends, FastAPI
from sqlalchemy.orm import Session
from app.models.models_moto import Moto
from app.schemas.schemas import MotoOut, CriarMoto,Atualizar
from typing import List
from app.database.session import get_db,SessionLocal

router = APIRouter()
# Instancia a aplicação Fastapi e o roteador
class MotoService:
    def __init__(self,db: Session = Depends(get_db)):
        self.db = db

    def service_criar_moto(self,criar: CriarMoto) -> MotoOut:
        nova_moto = Moto(**criar.model_dump())
        self.db.add(nova_moto)
        self.db.commit()
        self.db.refresh(nova_moto)
        return MotoOut.model_validate(nova_moto)
    
    def service_listar_motos(self) -> List[MotoOut]:
        motos = self.db.query(Moto).all()
        return [MotoOut.model_validate(c) for c in motos]
    
    def service_atualizar_moto(self,id: int,at: Atualizar) -> MotoOut:
        moto = self.db.query(Moto).filter(Moto.id == id).first()
        if not moto:
            raise HTTPException(status_code=404, detail='Moto nao encontrada')
        
        if at.marca is not None:
            moto.marca = at.marca
        if at.modelo is not None:
            moto.modelo = at.modelo
        
        self.db.commit()
        self.db.refresh(moto)
        return moto
    
    def service_deletar_moto(self,id: int) -> dict:
        moto = self.db.query(Moto).filter(Moto.id == id).first()
        if not moto:
            raise HTTPException(status_code=404,detail='Moto nao encontrada')

        self.db.delete(moto)
        self.db.commit()
        return {'mensagem':'Moto deletada com sucesso'}


'''
@router.get("/ping")
def ping_db(db: Session = Depends(get_db)):
    try:
        users = db.query(Users).all()
        return {"usuarios": [u.username for u in users]}
    except Exception as e:
        return {"erro": str(e)}

@router.get('/receber10')
def receber():
    return {'mensagem':'parabens pelo deploy dev'}

# Endpoint para criar uma nova moto
@router.post('/enviar1',response_model=MotoOut)
def enviar(criar: CriarMoto,db: Session = Depends(get_db)):
    nova_moto = Moto(**criar.dict())
    db.add(nova_moto)
    db.commit()
    db.refresh(nova_moto)
    return nova_moto

# Endpoint para listar todas as motos
@router.get('/receber1')
def receber(db: Session = Depends(get_db)):
    return db.query(Moto).all()

# Endpoint para atualizar uma moto existente
@router.put('/trocar1/{id}',response_model=MotoOut)
def trocar(id: int,at: Atualizar,db: Session = Depends(get_db)):
    info = db.query(Moto).filter(Moto.id == id).first()
    if not info:
        raise HTTPException(status_code=404,detail='moto nao encontrada')
    if at.marca is not None:
        info.marca = at.marca
    if at.modelo is not None:
        info.modelo = at.modelo
    db.commit()
    db.refresh(info)
    return info

# Endpoint para deletar uma moto
@router.delete('/deletar1/{id}')
def deletar(id: int,db: Session = Depends(get_db)):
    info = db.query(Moto).filter(Moto.id == id).first()
    if not info:
        raise HTTPException(status_code=404,detail='moto nao encontrada')
    db.delete(info)
    db.commit()
    return {'mensagem':'moto deletada com sucesso'}
'''
