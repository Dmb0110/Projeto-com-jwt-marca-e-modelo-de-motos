# auth/routes.py
'''
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import UserCreate, Token,CriarMoto,MotoOut
from .auth import authenticate_user, create_access_token,get_current_user
from crud import get_db
from models import Moto

router = APIRouter()

@router.post("/login", response_model=Token)
def login(user_data: UserCreate, db: Session = Depends(get_db)):
    user = authenticate_user(db, user_data.username, user_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post('/enviar',response_model=MotoOut)
def enviar(criar: CriarMoto,db: Session = Depends(get_db),current_user: Moto = Depends(get_current_user)):
    current_user.marca = criar.marca
    current_user.modelo = criar.modelo
    nova_moto = Moto(**criar.dict())
    db.commit()
    db.refresh(current_user)
    return current_user

from fastapi import APIRouter, Depends, HTTPException
from networkx.algorithms.connectivity import build_auxiliary_node_connectivity
from sqlalchemy.orm import Session
from schemas import UserCreate, Token, CriarMoto, MotoOut,Atualizar
from autenticacao2.auth import authenticate_user, create_access_token, get_current_user,get_password_hash
from models import Moto, User
from crud import get_db
from typing import List

router = APIRouter()

@router.post("/register", response_model=Token)
def register(user_data: UserCreate, db: Session = Depends(get_db)):
    hashed_password = get_password_hash(user_data.password)
    new_user = User(username=user_data.username, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    access_token = create_access_token(data={"sub": new_user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/login", response_model=Token)
def login(user_data: UserCreate, db: Session = Depends(get_db)):
    user = authenticate_user(db, user_data.username, user_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}
#######################################################################################3
@router.post("/enviar2", response_model=MotoOut)
def enviar(criar: CriarMoto, db: Session = Depends(get_db),
           current_user: User = Depends(get_current_user)):
    nova_moto = Moto(**criar.dict(), dono_id=current_user.id)
    db.add(nova_moto)
    db.commit()
    db.refresh(nova_moto)
    return nova_moto

@router.get('/receber2',response_model=List[MotoOut])
def receber(db: Session = Depends(get_db),
            current_user: User = Depends(get_current_user)):
    motos = db.query(Moto).filter(Moto.dono_id == current_user.id).all()
    return motos

@router.put('/trocar2/{id}')
def trocar(id: int,at: Atualizar,db: Session = Depends(get_db),
            current_user: User = Depends(get_current_user)):
    print(f"Tentando atualizar moto ID {id} para usuário {current_user.id}")
    info = db.query(Moto).filter(Moto.id == id, Moto.dono_id == current_user.id).first()

    if not info:
        print("Moto não encontrada ou não pertence ao usuário")
        raise HTTPException(status_code=404, detail='Moto não encontrada ou não pertence ao usuário')

    print("Dados recebidos para atualização:", at.dict(exclude_unset=True))

    for campo, valor in at.dict(exclude_unset=True).items():
        setattr(info, campo, valor)

    db.commit()
    db.refresh(info)
    return info

    if at.marca is not None:
        info.marca = at.marca
    if at.modelo is not None:
        info.modelo = at.modelo

'''


