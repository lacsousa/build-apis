# Resumo de Comandos do UV e FastAPI

## Criar ambiente virtual e inicializar

- `curl -LsSf https://astral.sh/uv/install.sh | sh` - Instala o UV (gerenciador de pacotes e ambientes).
- `uv init`: Inicializa um novo projeto gerenciado pelo uv, criando o ambiente virtual e arquivos de configuração (como `pyproject.toml`).
- `uv venv`: Cria um novo ambiente virtual python isolado no diretório atual (geralmente em `.venv`).
- `source .venv/bin/activate`: Ativa a venv no terminal (Linux/macOS).

## Instalação e Gerenciamento de Dependências

- `uv add "fastapi[standard]"`: Adiciona o FastAPI e suas dependências padrão (incluindo o servidor embutido uvicorn e ferramentas de CLI).
- `uv list` / `uv pip list`: Lista todos os pacotes e dependências instaladas no ambiente atual.
- `uv pip freeze > requirements.txt`: Cria o arquivo listando todas as dependências exatas do projeto.
- `uv pip install -r requirements.txt`: Instala as dependências a partir do arquivo requirements.txt.

## Execução do projeto FastAPI

- `uv run fastapi dev`: Inicia o servidor local de desenvolvimento na porta 8000 com o recurso de "hot-reload" ativado (reinicia automaticamente ao salvar os arquivos). Por padrão ele procura o objeto `app` no arquivo `main.py` ou `app.py`.

- `uv run fastapi run`: Inicia o servidor em modo de produção (sem hot-reload).

## Validação de Dados (Pydantic)

- O FastAPI utiliza o **Pydantic** debaixo dos panos para validar os dados das requisições (como o corpo de um POST). Você cria classes que herdam de `BaseModel`.

```python
from pydantic import BaseModel

class MeuModelo(BaseModel):
    campo1: int
    campo2: str
```

## Documentação Automática

Com o servidor em execução, o FastAPI gera automaticamente interfaces de documentação interativas que podem ser acessadas pelo navegador:
- **Swagger UI**: `http://localhost:8000/docs` (Permite testar a API diretamente pelo navegador)
- **ReDoc**: `http://localhost:8000/redoc` (Layout alternativo de documentação)
