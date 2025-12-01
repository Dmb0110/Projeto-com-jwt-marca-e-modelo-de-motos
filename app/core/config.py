import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente do arquivo .env
# Isso permite separar configuração sensível (como credenciais) do código.
load_dotenv()

class Settings:
    # Aqui você está apenas atribuindo diretamente a variável.
    # Se DATABASE_URL não estiver definida no .env, o valor será None.
    DATABASE_URL: str = os.getenv('DATABASE_URL')

# Cria uma instância única de Settings para ser usada em todo o projeto.
# Isso centraliza as configurações e evita chamadas repetidas a os.getenv.
settings = Settings()
