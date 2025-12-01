from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.session import Base

# Modelo da tabela 'users' usando SQLAlchemy 2.0 com tipagem moderna (Mapped).
class User(Base):
    __tablename__ = 'users'

    # id como chave primária, com índice para consultas mais rápidas.
    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    # username único e não nulo, com limite de 50 caracteres.
    # Sugestão: considerar normalizar (ex: lowercase) para evitar duplicidade com maiúsculas/minúsculas.
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)

    # hashed_password armazenado como string.
    # Sugestão: aumentar o tamanho da coluna (ex: String(255)) porque hashes bcrypt podem ultrapassar 50 caracteres.
    hashed_password: Mapped[str] = mapped_column(String(50), nullable=False)

    # Se houver relacionamento com outras tabelas (ex: motos), pode-se adicionar:
    # motos: Mapped[list["Moto"]] = relationship("Moto", back_populates="usuario")
