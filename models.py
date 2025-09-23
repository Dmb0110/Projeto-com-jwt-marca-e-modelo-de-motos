from fastapi import FastAPI
from sqlalchemy import Column, Integer, String, create_engine,ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker,relationship

DATABASE_URL = "postgresql://postgres:davi9090@localhost:5432/banco_dmb"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)

class Moto(Base):
    __tablename__ = 'motos'

    id = Column(Integer, primary_key=True, index=True)
    marca = Column(String)
    modelo = Column(String)
    #  Essa coluna se relaciona com a coluna [id] da tabela [users]
    dono_id = Column(Integer, ForeignKey('users.id'))


'''
DATABASE_URL =

engine = create_egine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer,prinmary_key=True,index=True)
    username = Column(String)
    password = Column(String)

class Cliente(Base):
    __tablename__ = 'clientes'

    id = Column(Integer,primary_key=True,index=True)
    nome = Column(String)
    idade = Column(Integer)




DATABASE_URL =

engine = create_engine(DATABASE_URL)
SessionLocel = sessionmaker(bind=engine,autocommit=True,autoflush=True)
Base = declarative_base()

class User(Base):
    id = Column(primary_key=True,index=True)
    username = Column(String)
    password = Column(String)

class Moto(Base):
    id = Column(primary_key=True,index=True)
    marca = Column(String)
    modelo = Column(String)










DATABASE_URL =

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine,autocommit=True,autflush=True)
Base = declarative_base()

class User(Base):
    id = Column(Integer,primary_key=True,index=True)
    username = Column(String)
    password = Column(String)

class Tv(Base):
    id = Column(Integer,primary_key=True,index=True)
    marca = Column(String)
    polegadas = Column(Integer)

'''



