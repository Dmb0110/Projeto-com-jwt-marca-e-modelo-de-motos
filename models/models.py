from fastapi import FastAPI
from sqlalchemy import Column, Integer, String, create_engine,ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker,relationship

# URL de conexão com o banco PostgreSQL
DATABASE_URL = "postgresql://postgres:davi9090@localhost:5432/banco_dmb"

# Cria o motor de conexão com o banco
engine = create_engine(DATABASE_URL)

# Configura a sessão para interagir com o banco
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Base para definição dos modelos
Base = declarative_base()

# Modelo da tabela 'users'
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)

# Modelo da tabela 'motos'
class Moto(Base):
    __tablename__ = 'motos'

    id = Column(Integer, primary_key=True, index=True)
    marca = Column(String)
    modelo = Column(String)
    #  Essa coluna se relaciona com a coluna [id] da tabela [users]
    dono_id = Column(Integer, ForeignKey('users.id'))
