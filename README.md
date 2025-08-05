# HR Management System

Este projeto demonstra um sistema básico de gestão de RH com autenticação e controle de metas.

## Backend (FastAPI)
- Localizado em `backend/`
- Dependências em `backend/requirements.txt`
- Executar localmente:
  ```bash
  pip install -r backend/requirements.txt
  uvicorn app.main:app --reload --app-dir backend
  ```
- Endpoints principais:
  - `POST /auth/register`
  - `POST /auth/login`
  - `GET /users/me`
  - `POST /goals/`
  - `GET /goals/`

## Frontend (Vue 3 + Vite)
- Localizado em `frontend/`
- Para executar:
  ```bash
  cd frontend
  npm install
  npm run dev
  ```
  A aplicação estará em `http://localhost:5173`.

## Banco de Dados
- Por padrão utiliza SQLite para desenvolvimento.
- Para usar PostgreSQL defina a variável `DATABASE_URL`, por exemplo:
  `export DATABASE_URL=postgresql://usuario:senha@localhost:5432/banco`

## Testes
- Há testes básicos para o backend:
  ```bash
  pytest
  ```
