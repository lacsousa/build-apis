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

## Linting e Qualidade de Código com Ruff

- `uv add --dev ruff`: adiciona o `ruff` como dependência de desenvolvimento no projeto.
- `uv run ruff check .`: verifica o código Python em busca de problemas de estilo, erros e formatação.
- `uv run ruff format .`: formata automaticamente os arquivos Python suportados pelo `ruff`.
- `ruff` é uma ferramenta rápida de lint/format para Python, que substitui e unifica regras de `flake8`, `isort`, `black`, `mypy` e outros em um único runner.

## Automatização com Pre-Commit Hooks

Para garantir que o código esteja sempre bem formatado e livre de erros antes de cada commit, utilizamos o **pre-commit**.

1. **Instalar o pre-commit globalmente (ou no ambiente):**
   ```bash
   pip install pre-commit
   # ou usando uv
   uv pip install pre-commit
   ```

2. **Instalar os hooks de commit no repositório Git:**
   Execute a partir da raiz do repositório:
   ```bash
   pre-commit install
   ```

3. **Executar manualmente em todos os arquivos:**
   Se quiser testar todos os arquivos sem fazer um commit:
   ```bash
   pre-commit run --all-files
   ```
   *(Nota: Se o arquivo de configuração `.pre-commit-config.yaml` estiver em uma subpasta como `Django/`, execute o comando de dentro dessa pasta).*

---

## Problemas Comuns e Soluções (Troubleshooting)

### 1. Erro: `zsh: command not found: ruff` ou `Failed to spawn: ruff`
* **Causa**: O `ruff` não está instalado no seu ambiente de terminal global ou no ambiente virtual ativo.
* **Solução**:
  * **Solução Temporária (sem instalar)**: Use o `uvx` para rodar diretamente:
    ```bash
    uvx ruff check .
    ```
  * **Solução Definitiva**: Entre na pasta do projeto (ex: `cd Django` ou `cd Exemplo-01`), adicione o ruff ao projeto e execute com `uv run`:
    ```bash
    uv add --dev ruff
    uv run ruff check .
    ```

### 2. Erro: `uv run` ou `uv pip list` usando o ambiente Python global
* **Causa**: Você executou o comando a partir da raiz do repositório (`build-apis`), mas o repositório raiz não é um projeto Python configurado (não tem `pyproject.toml` ou `.venv` na raiz).
* **Solução**: Navegue para a pasta do subprojeto específico antes de rodar os comandos do `uv` ou ativar a virtualenv:
  ```bash
  cd Django            # para o projeto Django
  # ou
  cd Exemplo-01        # para o projeto FastAPI
  ```

### 3. Erro: `pre-commit` falha com `Failed` em hooks de formatação (ex: `ruff-format`, `trailing-whitespace`, `end-of-file-fixer`)
* **Causa**: Os arquivos não seguiam as regras de formatação (tinham espaços extras no final das linhas, não terminavam com quebra de linha ou o formato de código do Python estava incorreto).
* **Solução**: O próprio `pre-commit` corrige esses problemas automaticamente nos arquivos físicos. Quando isso acontecer:
  1. Veja quais arquivos foram modificados pelo hook (ex: usando `git status`).
  2. Adicione as correções feitas ao stage: `git add .` (ou arquivos específicos).
  3. Tente fazer o commit novamente: `git commit -m "sua mensagem"`.

### 4. Erro: `pre-commit` falha com erros de lógica no Ruff (`F811`, `F821`, etc.)
* **Causa**: O linter detectou erros reais de código (como funções redefinidas com o mesmo nome ou variáveis indefinidas).
* **Solução**: Esses erros não podem ser corrigidos automaticamente e exigem correção manual no código fonte. Após corrigir os arquivos, adicione-os no git com `git add` e tente commitar novamente.

