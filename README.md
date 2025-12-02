# API de Motos

## Descrição
API desenvolvida em **FastAPI** para gerenciar motos.  
Permite cadastrar e consultar motos informando **marca** e **modelo**.

------------------------------------------------------

## ⚙️ Tecnologias utilizadas
- **Python 3.13.0** → linguagem principal do projeto
- **FastAPI** → framework web moderno e assíncrono
- **SQLAlchemy** → ORM para manipulação do banco de dados
- **Alembic** → ferramenta de migração de banco de dados
- **PostgreSQL (Neon)** → banco de dados relacional utilizado
- **Autenticação: JWT** → controle de acesso com tokens
- **Servidor: Uvicorn** → servidor ASGI para rodar a aplicação
- **Ferramentas de testes: Pytest** → testes automatizados

------------------------------------------------------

## Instalação e execução

1. Clone o repositório:
   ```bash
   git clone https://github.com/Dmb0110/Projeto-com-jwt-marca-e-modelo-de-motos.git
   cd projeto3 autenticacao jwt

------------------------------------------------------
## (Visão geral do projeto)
Título: Nome claro do projeto (ex.: “projeto com jwt marca e modelo de motos”).

Descrição: Permite adicionar,listar,trocar os dados e deletar marcas e modelos de varias motos.

Principais recursos: Cadastro e listagem de motos por marca e modelo.

Tecnologias: Python, FastAPI, SQLAlchemy, Alembic, PostgreSQL (Neon).

------------------------------------------------------
## (Pré-requisitos)
Versões: Python 3.13.0, PostgreSQL 17.

Dependências: FastAPI, Uvicorn, SQLAlchemy, Alembic, psycopg2.

Acesso ao banco: String de conexão válida (ex.: Neon com sslmode).

------------------------------------------------------
## [CONFIGURAÇAO E INSTALAÇAO]
## (Clonar o repositório):

git clone https://github.com/Dmb0110/Projeto-com-jwt-marca-e-modelo-de-motos.git
cd projeto3 autenticacao jwt

-----------------------------------------------------
## (Criar/ativar ambiente virtual):

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

-----------------------------------------------------
## (Instalar dependências):


pip install -r requirements.txt

-----------------------------------------------------
## (Variáveis de ambiente (.env)):

DATABASE_URL=postgresql+psycopg2://usuario:senha@host:5432/nome_do_banco?sslmode=require


-----------------------------------------------------
## (Configurar Alembic (se aplicável)):

Verifique alembic.ini e alembic/env.py apontando para DATABASE_URL.

-----------------------------------------------------
## (Migrações e execução)
Aplicar migrações:

alembic upgrade head
Rodar servidor:

uvicorn app.main:app --reload

-----------------------------------------------------
## (URLs de documentação):

Swagger: http://localhost:8000/docs

ReDoc: http://localhost:8000/redoc

-----------------------------------------------------
## (Endpoints da API)
Criar moto (POST /motos):

Body:

json
{
  "marca": "Honda",
  "modelo": "CG 160"
}

-----------------------------------------------------
## Resposta:

json
{
  "id": 1,
  "marca": "Honda",
  "modelo": "CG 160"
}

-----------------------------------------------------
## Listar motos (GET /motos):

Resposta:

json
[
  { "id": 1, "marca": "Honda", "modelo": "CG 160" },
  { "id": 2, "marca": "Yamaha", "modelo": "Fazer 250" }
]
-----------------------------------------------------
## 🔐 Autenticação com JWT

Este projeto utiliza **JSON Web Tokens (JWT)** para autenticação e autorização.  
Usuários devem se registrar e fazer login para obter um token de acesso.  
Esse token deve ser enviado no cabeçalho das requisições para acessar endpoints protegidos.

### Fluxo de autenticação
1. **Registro de usuário**  
   `POST /registro`  
   Body:
   ```json
   {
     "username": "joao",
     "password": "senha123"
   }

-----------------------------------------------------
## (Modelo de dados e validação)
**Entidade Moto: campos mínimos**

id: inteiro autoincremento.
marca: string obrigatória.
modelo: string obrigatória.

Regras básicas:

Marca/modelo não vazios: validar no schema (Pydantic).

Erros comuns: retornar 422 para payload inválido.

**Entidade User**

id: inteiro autoincremento
username: string obrigatoria,único (não pode repetir)
password: string obrigatoria,armazenada com hash (não em texto puro)

Validações:

Username não pode ser vazio e deve ser único
Password deve ser validado e armazenado com hashing seguro (ex: **bcrypt** viar Passlib) 
Retornar 422 em caso de payload inválido


## Autenticação
- Usuários devem se registrar e fazer login para obter um **JWT token**  
- O token deve ser enviado no cabeçalho: 

-------------------------------------------------------
## (Testes e qualidade)
Rodar testes:

pytest

-------------------------------------------------------
## (Deploy (opcional))
Container: Dockerfile e docker-compose para app + banco.

Variáveis de produção: DATABASE_URL segura

Health check: endpoint simples (ex.: GET /health retornando 200).

------------------------------------------------------
## 📂 Estrutura do projeto
app/
 ├── main.py
 ├── core/config.py
 ├── crud_services/        # 4 arquivos
 ├── database/session.py
 ├── models/               # 2 arquivos
 ├── routers/              # 4 arquivos
 ├── schemas.py
 └── db.py

alembic/                   # migrações
requirements.txt           # dependências
README.md                  # documentação

-----------------------------------------------------
