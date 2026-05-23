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

## Common Issues
- **Missing migrations**: Run `python manage.py makemigrations` then `migrate`.
- **Port already in use**: Change the port with `python manage.py runserver 0.0.0.0:8001`.
- **Environment variables**: Adjust settings in `sistema/settings.py` (e.g., `DEBUG`, `ALLOWED_HOSTS`).

---
*Keep this file updated as the project evolves.*
