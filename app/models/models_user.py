from sqlalchemy import Integer,String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.session import Base

# Modelo da tabela 'users'
class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(50),nullable=False)
