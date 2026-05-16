# Exemplo 01 - FastAPI com UV

Este é um exemplo básico de como iniciar um projeto FastAPI utilizando o gerenciador de pacotes e ambientes **uv**.

## 1. Instalar o `uv`

O `uv` é um gerenciador de pacotes e projetos para Python extremamente rápido. Caso ainda não o tenha instalado, utilize o comando abaixo (para macOS e Linux):

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
*(Para usuários de Windows, utilize o powershell: `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`)*

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
- **Documentação Interativa (Swagger UI):** Acesse [http://localhost:8000/docs](http://localhost:8000/docs) para visualizar e interagir graficamente com todas as rotas da sua API. Nela, você pode testar as requisições usando o botão *"Try it out"* e depois *"Execute"*.
