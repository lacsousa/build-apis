# Django API Project – build-apis

## Overview
This repository contains a **Django** based REST API project named **build-apis**. The main application lives under the `sistema` package, while the API layer (serializers, views, and URLs) is in the `api` package.

## Project Structure
```
Django/
├─ api/
│   ├─ __init__.py
│   ├─ models.py
│   ├─ serializers.py
│   ├─ views.py      # API views (ModelViewSet, function‑based, class‑based)
│   └─ urls.py       # API specific routes (optional)
├─ sistema/
│   ├─ __init__.py
│   ├─ settings.py   # Project settings (JWT, drf_yasg, REST framework)
│   ├─ urls.py       # Root URL configuration
│   └─ wsgi.py
├─ manage.py
├─ notes.md         # Project notes (quick start, common issues, etc.)
└─ .gitignore
```

## Quick Start
1. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
2. **Install dependencies** (ensure `requirements.txt` contains `Django`, `djangorestframework`, `drf-yasg`, `djangorestframework‑simplejwt`)
   ```bash
   pip install -r requirements.txt
   ```
3. **Apply migrations**
   ```bash
   python manage.py migrate
   ```
4. **Run the development server**
   ```bash
   python manage.py runserver
   ```
   The API will be available at `http://127.0.0.1:8000/`.

## API Endpoints
| Endpoint | Method | Description |
|---|---|---|
| `/soma/<int:numero1>/<int:numero2>/` | GET | Simple sum (v1) – returns `{"resultado": <total>}` |
| `/soma/v2/` | POST | Sum via JSON payload `{ "numero1": int, "numero2": int }` (v2) |
| `/soma/v3/` | POST | Sum via class‑based view with OpenAPI schema (v3) |
| `/empresa/` | GET/POST/PUT/DELETE | CRUD operations for `Empresa` model (via `ModelViewSet`) |
| `/swagger/` | GET | Interactive API docs (drf‑yasg) |
| `/api/token/` | POST | Obtain JWT (provide `username` & `password`) |
| `/api/token/refresh/` | POST | Refresh JWT |
| `/api/token/verify/` | POST | Verify JWT |

## Authentication (JWT)
The project uses **Simple JWT**:
- Add `rest_framework_simplejwt.authentication.JWTAuthentication` to `DEFAULT_AUTHENTICATION_CLASSES` in `settings.py`.
- Protect views by adding `permission_classes = [permissions.IsAuthenticated]` where needed.
- Obtain a token via `POST /api/token/` with credentials.

## Swagger / OpenAPI
Swagger UI is available at `/swagger/` (and Redoc at `/redoc/`). The `SomaFormato2View` demonstrates how to add request/response schemas using **drf‑yasg**.

## Notes
For more detailed information, see [notes.md](notes.md) – it contains quick‑start steps, common issues, and reminders to keep this file updated as the project evolves.

## Common Issues
- **Missing migrations**: Run `python manage.py makemigrations` then `python manage.py migrate`.
- **Port already in use**: Change the port with `python manage.py runserver 0.0.0.0:8001`.
- **Environment variables**: Adjust settings in `sistema/settings.py` (e.g., `DEBUG`, `ALLOWED_HOSTS`).

---
*Keep this README updated as the project evolves.*
