from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from app.core.config import settings

# Cria o engine usando a DATABASE_URL definida nas configurações.
# Sugestão: adicionar parâmetros como pool_pre_ping=True e echo=False para maior robustez.
engine = create_engine(settings.DATABASE_URL)

# Cria a fábrica de sessões (SessionLocal).
# autocommit=False e autoflush=False são boas práticas para controle explícito das transações.
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Base declarativa para os modelos ORM.
Base = declarative_base()

def get_db():
    # Cria uma nova sessão para cada requisição.
    db = SessionLocal()
    try:
        # Usa yield para permitir que FastAPI injete a sessão como dependência.
        yield db
    finally:
        # Fecha a sessão após o uso, evitando vazamento de conexões.
        db.close()
