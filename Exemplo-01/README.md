# Exemplo 01 - FastAPI com UV

Este é um exemplo básico de como iniciar um projeto FastAPI utilizando o gerenciador de pacotes e ambientes **uv**.

## 1. Instalar o `uv`

O `uv` é um gerenciador de pacotes e projetos para Python extremamente rápido. Caso ainda não o tenha instalado, utilize o comando abaixo (para macOS e Linux):

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

_(Para usuários de Windows, utilize o powershell: `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`)_

## 2. Adicionar o FastAPI

Com o `uv` instalado e dentro do diretório do seu projeto (onde está o seu `main.py`), você pode instalar o FastAPI e todas as suas dependências padrão (incluindo o servidor uvicorn) usando:

```bash
uv add "fastapi[standard]"
```

## 3. Rodar o Servidor Local

Para rodar a sua API e testá-la na sua máquina local com recarregamento automático (hot-reload), execute:

```bash
uv run fastapi dev main.py
```

## 4. Testar a API

Com o servidor rodando, você pode acessar a sua API de duas formas através do navegador:

- **Rota Raiz:** Acesse [http://localhost:8000/](http://localhost:8000/) para ver a resposta inicial (ex: `{"Hello": "from exemplo-01!"}`).
- **Documentação Interativa (Swagger UI):** Acesse [http://localhost:8000/docs](http://localhost:8000/docs) para visualizar e interagir graficamente com todas as rotas da sua API. Nela, você pode testar as requisições usando o botão _"Try it out"_ e depois _"Execute"_.

## Mudanças recentes (refatoração)

- Separei responsabilidade em módulos: agora há um pacote `api` com submódulos `models`, `utils`, `services` e `routers`.
- `api/services.py`: centraliza o cliente OpenAI (`openai_client`) e o carregamento de variáveis de ambiente.
- `api/routers/operacoes_router.py` e `api/routers/llm_router.py`: rotas convertidas para `APIRouter` e registradas em `api/main.py`.
- `api/utils.py`: funções auxiliares (`get_logger`, `common_api_token`, `execute_prompt`) atualizadas para usar `api.services.openai_client`.
- Adicionados testes em `tests/test_api.py` (8 testes, incluindo mock do cliente OpenAI e validação de autenticação).

Se você usa o servidor dev com `uv`, rode a partir da raiz do projeto:

```bash
uv run fastapi dev api/main.py
```

Se a porta 8000 já estiver em uso, inicie em outra porta:

```bash
uv run fastapi dev api/main.py --port 8001
```

Para executar a suíte de testes:

```bash
uv run pytest tests/test_api.py -v
```

Para rodar com saída resumida:

```bash
uv run pytest tests/test_api.py -q
```

## Rodando com Docker

Certifique-se de ter o arquivo `.env` criado a partir do `.example-env`:

```bash
cp .example-env .env
# edite o .env e adicione sua OPENAI_API_KEY
```

Suba o container:

```bash
docker compose up --build
```

A API estará disponível em `http://localhost:8000` e a documentação em `http://localhost:8000/docs`.

> Para rodar junto com o projeto Django na porta 8001, use o `docker-compose.yml` na raiz do repositório.
