from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.session import Base

# Modelo da tabela 'motos'
class Moto(Base):
    __tablename__ = 'motos'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    marca: Mapped[str] = mapped_column(String(100),nullable=False)
    modelo: Mapped[str] = mapped_column(String(100),nullable=False)
    #ano: Mapped[int] = mapped_column(nullable=False)

    #dono_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)
    
    #  Essa coluna se relaciona com a coluna [id] da tabela [users]
    #dono: Mapped['User'] = relationship(back_populates='motos')
    