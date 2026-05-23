# 🚀 Construção de APIs para Inteligência Artificial

**UFG - Universidade Federal de Goiás**  
👨‍🏫 **Professor:** Rogério Rodrigues Carvalho

Bem-vindo ao repositório de projetos e estudos da disciplina de **Construção de APIs para IA**. Aqui você encontrará os exercícios, exemplos práticos e anotações feitas ao longo das aulas.

---

## 📂 O que já temos por aqui?

✅ **[Exemplo-01: Primeira API com FastAPI](./Exemplo-01/)**

- ⚡ Configuração super rápida do ambiente utilizando o gerenciador `uv`.
- 🛠️ Criação de uma API básica com o framework **FastAPI**.
- 📖 Execução do servidor local com acesso à documentação interativa gerada automaticamente (Swagger UI).

📝 **[Anotações e Guias de Estudo](./notes.md)**

- 📓 Arquivo centralizando comandos úteis, anotações de aula e guias de referência rápida (abrangendo ferramentas e frameworks estudados até o momento).

---

## 🛠️ Stack Tecnológica (Até o momento)

- 🐍 **Python**
- ⚡ **FastAPI**
- 📦 **uv** (Gerenciador de pacotes e projetos)

---

## 🔄 Atualizações recentes (Exemplo-01)

- **Endpoint novo:** `POST /historia` em `Exemplo-01/main.py` — gera uma história a partir de um tema usando a OpenAI.
  - Corpo esperado (JSON): `{ "tema": "seu tema aqui" }`
  - Retorno (JSON): `{ "tema": "...", "historia": "..." }`
  - Observação: a rota aceita somente `POST`. Acessar `http://127.0.0.1:8000/historia` por `GET` retorna `405 Method Not Allowed`.

- **Integração com OpenAI:** o projeto chama a API da OpenAI (via biblioteca `openai`) para gerar o texto.
  - A aplicação carrega a chave `OPENAI_API_KEY` a partir de variáveis de ambiente. Opcionalmente é possível colocar a chave em um arquivo `.env` na raiz de `Exemplo-01`.
  - ATENÇÃO: a chave no `.env` deve estar em **uma única linha** no formato `OPENAI_API_KEY=sk-...` (não quebrar em múltiplas linhas).

- **Carregamento do .env:** `main.py` agora usa `python-dotenv` (`load_dotenv()`) para carregar variáveis do `.env` automaticamente.

- **Dependências adicionadas/atualizadas** (em `Exemplo-01/pyproject.toml`): `openai`, `python-dotenv`.

## ▶️ Como rodar localmente (Exemplo-01)

1. Entre na pasta do exemplo e ative a virtualenv:

```bash
cd Exemplo-01
source .venv/bin/activate
```

2. Instale dependências necessárias (exemplo mínimo):

```bash
# Recomendado: use o gerenciador de projetos `uv` configurado para este repositório.
# Exemplo genérico (se o seu projeto define um script de instalação):
uv run install

# Alternativa: instalar manualmente com pip
python -m pip install --upgrade pip
python -m pip install openai python-dotenv uvicorn[standard]
```

3. Ajuste o arquivo `.env` (se estiver usando):

Você pode criar o arquivo `.env` copiando o exemplo fornecido `.example-env`:

```bash
cp .example-env .env
```

Caso prefira editar manualmente, garanta que a variável esteja em uma única linha:

```env
OPENAI_API_KEY=sk-...   # tudo em uma linha
```

4. Inicie o servidor:

```bash
python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

5. Exemplo de chamada `curl` para o endpoint `POST /historia`:

```bash
curl -X POST http://127.0.0.1:8000/historia \
    -H "Content-Type: application/json" \
    -d '{"tema": "um dragão que aprende a amar livros"}'
```

## 🐞 Problemas comuns e solução rápida

- `405 Method Not Allowed` ao acessar a URL no navegador: use `POST` em vez de `GET`.
- `{"detail": "OPENAI_API_KEY não configurada..."}`: verifique se a variável está definida no mesmo terminal onde o servidor é iniciado, ou corrija o arquivo `.env` (chave em uma única linha) e reinicie o servidor.

---

## 🐍 Django API – build-apis

**Projeto Django** localizado em `Django/` fornece uma API RESTful completa com recursos de CRUD, soma simples, autenticação JWT e documentação Swagger.

### Estrutura de Diretórios
```
build-apis/
├─ Django/
│   ├─ api/
│   │   ├─ __init__.py
│   │   ├─ models.py
│   │   ├─ serializers.py
│   │   ├─ views.py      # ModelViewSet, function‑based & class‑based views
│   │   └─ urls.py       # (opcional) rotas específicas da API
│   ├─ sistema/
│   │   ├─ __init__.py
│   │   ├─ settings.py   # inclui rest_framework, drf_yasg, simplejwt
│   │   ├─ urls.py       # rotas raiz, JWT endpoints, Swagger UI
│   │   └─ wsgi.py
│   ├─ manage.py
│   ├─ notes.md         # notas rápidas para o projeto Django
│   └─ .gitignore
├─ Exemplo-01/          # Projeto FastAPI (mantido)
├─ notes.md             # notas gerais do repositório
└─ README.md            # (este documento)
```

### Como iniciar o projeto Django
1. **Criar e ativar ambiente virtual**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
2. **Instalar dependências** (verifique `requirements.txt` em `Django/`)
   ```bash
   pip install -r Django/requirements.txt
   # ou manualmente:
   pip install Django djangorestframework drf-yasg djangorestframework-simplejwt
   ```
3. **Aplicar migrações**
   ```bash
   cd Django
   python manage.py migrate
   ```
4. **Criar super‑user (opcional)**
   ```bash
   python manage.py createsuperuser
   ```
5. **Rodar o servidor de desenvolvimento**
   ```bash
   python manage.py runserver
   ```
   A API estará disponível em `http://127.0.0.1:8000/`.

### Principais Endpoints da API Django
| Rota | Método | Descrição |
|------|--------|-----------|
| `/soma/<int:numero1>/<int:numero2>/` | GET | Soma simples (versão 1) |
| `/soma/v2/` | POST | Soma via payload JSON (versão 2) |
| `/soma/v3/` | POST | Classe baseada com schema OpenAPI (versão 3) |
| `/empresa/` | GET/POST/PUT/DELETE | CRUD para o modelo `Empresa` |
| `/swagger/` | GET | UI interativa da documentação (drf‑yasg) |
| `/api/token/` | POST | Obter JWT (username & password) |
| `/api/token/refresh/` | POST | Refresh do JWT |
| `/api/token/verify/` | POST | Verificar JWT |

### Autenticação JWT
- Configurada em `settings.py` com `REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES']`.
- Para proteger vistas, adicione `permission_classes = [permissions.IsAuthenticated]`.
- Tokens são obtidos via `POST /api/token/`.

### Documentação Swagger
A UI Swagger está disponível em `http://127.0.0.1:8000/swagger/` e Redoc em `/redoc/`.

### Notas rápidas
- Veja o arquivo [`Django/notes.md`](Django/notes.md) para passos de setup, troubleshooting e próximos passos.
- Para atualizar dependências, ajuste `requirements.txt` dentro da pasta `Django/`.

---

Se quiser, eu atualizo também o `Exemplo-01/README.md` (dentro do diretório) com instruções específicas do projeto.
