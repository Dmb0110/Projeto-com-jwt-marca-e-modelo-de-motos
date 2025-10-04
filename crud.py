from fastapi import APIRouter, HTTPException, Depends, FastAPI
from sqlalchemy.orm import Session
from models.models import SessionLocal,Moto
from schemas import MotoOut, CriarMoto,Atualizar
from typing import List

# Instancia a aplicação Fastapi e o roteador
app = FastAPI()
router = APIRouter()

# Função para obter uma sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint para criar uma nova moto
@router.post('/enviar1',response_model=MotoOut)
def enviar(criar: CriarMoto,db: Session = Depends(get_db)):
    nova_moto = Moto(**criar.dict())
    db.add(nova_moto)
    db.commit()
    db.refresh(nova_moto)
    return nova_moto

# Endpoint para listar todas as motos
@router.get('/receber1',response_model=List[MotoOut])
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
