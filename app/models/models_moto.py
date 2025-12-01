from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.session import Base

# Modelo da tabela 'motos' usando SQLAlchemy 2.0 com tipagem moderna (Mapped).
class Moto(Base):
    __tablename__ = 'motos'

    # id como chave primária, com índice para consultas mais rápidas.
    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    # Campos marca e modelo com tamanho máximo de 100 caracteres e não nulos.
    marca: Mapped[str] = mapped_column(String(100), nullable=False)
    modelo: Mapped[str] = mapped_column(String(100), nullable=False)