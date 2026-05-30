Changelog - Refatoração (2026-05-23)

Resumo

- Refatorei a API para separar responsabilidades e facilitar testes.

Mudanças principais

- `api/services.py` criado: contém `openai_client` e carrega `.env`.
- Rotas movidas para `api/routers/operacoes_router.py` e `api/routers/llm_router.py` como `APIRouter`.
- `api/main.py` agora registra os routers em `app.include_router(...)`.
- `api/utils.py` atualizado: `common_api_token` aceita o modelo `Numeros`, `get_logger` e `execute_prompt` usam `api.services.openai_client`.
- Testes adicionados em `tests/test_api.py` com mock do cliente OpenAI (`monkeypatch` em `api.services.openai_client`).

Como testar localmente

1. Ative o virtualenv e instale dependências (se necessário).
2. Rodar servidor dev:

```bash
uv run fastapi dev api/main.py
```

3. Rodar testes:

```bash
pytest -q
```

Notas de implementação

- Não adicionei novas dependências externas; usei apenas as libs já presentes no projeto.
- O cliente OpenAI foi centralizado em `api/services.py` para evitar import cycles e permitir mock em testes.
- Se quiser commitar as mudanças, recomendo um commit com mensagem clara: "Refactor: split routers, services and utils; add tests".

Próximos passos recomendados

- Adicionar `requirements-dev.txt` com `pytest` e outras dev-deps.
- Opcional: adicionar `Makefile` ou `pyproject.toml` com tarefa `test` para simplifies testes.

---

## Docker

### Pré-requisito: arquivo .env

```bash
cp .example-env .env
# edite o .env e preencha OPENAI_API_KEY e API_TOKEN
```

### Subir o container (a partir de `Exemplo-01/`)

```bash
docker compose up --build
```

A API estará disponível em `http://localhost:8000` e o Swagger em `/docs`.

### Comandos úteis

```bash
docker compose down          # para e remove o container
docker compose logs -f web   # acompanha os logs em tempo real
```

> Para rodar junto com o Django, use o `docker-compose.yml` na raiz do repositório (`docker compose up --build` de lá). Nesse caso o FastAPI sobe na porta **8001**.


