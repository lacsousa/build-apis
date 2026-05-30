# Django Project Notes

## Overview
This repository contains a **Django** based API project named **build-apis**. The main application lives under the `sistema` package and the API serializers are defined in `api/serializers.py`.

## Project Structure
```
Django/
├─ api/                # API layer (serializers, views, urls)
│   └─ serializers.py
├─ sistema/            # Core Django project settings and URL routing
│   ├─ __init__.py
│   ├─ settings.py    # Project settings
│   └─ urls.py        # Root URL configuration
├─ manage.py           # Django management script
├─ notes.md            # ← This file – project notes
└─ .gitignore
```

## Quick Start
1. **Create virtual environment** (if not already):
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
2. **Install dependencies** (ensure `Django` is listed in `requirements.txt` or install directly):
   ```bash
   pip install -r requirements.txt   # or pip install Django
   ```
3. **Apply migrations**:
   ```bash
   python manage.py migrate
   ```
4. **Run development server**:
   ```bash
   python manage.py runserver
   ```
   The API will be available at `http://127.0.0.1:8000/`.

## Useful Commands
- **Create a new app**:
  ```bash
  python manage.py startapp myapp
  ```
- **Run tests**:
  ```bash
  python manage.py test
  ```
- **Open a Django shell**:
  ```bash
  python manage.py shell
  ```

## Extending the API
- Add new serializers in `api/serializers.py`.
- Wire up new endpoints in `api/urls.py` (create if missing) and include them in `sistema/urls.py`:
  ```python
  from django.urls import include, path
  urlpatterns = [
      path('api/', include('api.urls')),
      # other routes
  ]
  ```

## Docker

### Subir o container (a partir de `Django/`)

```bash
docker compose up --build
```

A API estará disponível em `http://localhost:8000` e o Swagger em `/swagger/`.

### Comandos úteis

```bash
docker compose down          # para e remove o container
docker compose logs -f web   # acompanha os logs em tempo real
docker compose exec web python manage.py createsuperuser  # cria superuser dentro do container
docker compose exec web python manage.py migrate          # roda migrações manualmente
```

> Para rodar junto com o Exemplo-01, use o `docker-compose.yml` na raiz do repositório (`docker compose up --build` de lá).

---

## Common Issues & Troubleshooting

- **Missing migrations**: Run `python manage.py makemigrations` then `migrate`.
- **Port already in use**: Change the port with `python manage.py runserver 0.0.0.0:8001`.
- **Environment variables**: Adjust settings in `sistema/settings.py` (e.g., `DEBUG`, `ALLOWED_HOSTS`).
- **Command not found / failed to spawn: `ruff`**:
  * **Causa**: O `ruff` não está instalado no `.venv` do Django.
  * **Solução**: Você pode rodar de forma avulsa usando `uvx ruff check .` ou adicioná-lo permanentemente ao projeto rodando `uv add --dev ruff`.
- **`pre-commit` Command Executions**:
  * **Uso**: O arquivo `.pre-commit-config.yaml` agora está localizado na **raiz do repositório** para que funcione globalmente (e no GitHub Actions). Para executar manualmente em todos os arquivos:
    ```bash
    pre-commit run --all-files
    ```
  * **Falha nos hooks de formatação**: Se o `pre-commit` acusar falha em hooks como `ruff-format` ou `trailing-whitespace` mas os arquivos foram modificados, basta fazer `git add .` das modificações automáticas e tentar o commit novamente.

---
*Keep this file updated as the project evolves.*
