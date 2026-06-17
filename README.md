# Tasks API

A small FastAPI service used as a realistic review target. It exposes user
registration, token login, task CRUD, and tag listing over SQLite.

This repository intentionally includes a mix of clean files and planted issues
so automated review tiers have useful signal across security, performance, and
quality dimensions.

## Local development

```bash
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

The API is available at `http://127.0.0.1:8000`.

## Endpoints

- `POST /auth/register`
- `POST /auth/login`
- `GET /users`
- `GET /tasks`
- `POST /tasks`
- `PATCH /tasks/{task_id}`
- `GET /tags`
- `POST /tags`

## Test

```bash
pytest
```
