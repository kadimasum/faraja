# Faraja - Government Project Accountability Platform

Faraja is a fullstack application for tracking implementation of government projects and increasing public accountability.

## Stack

- Frontend: Next.js (TypeScript)
- Backend: FastAPI (Python)
- Database: PostgreSQL

## Project Structure

- `frontend/`: Next.js dashboard for creating and viewing projects
- `backend/`: FastAPI API with project and milestone endpoints
- `docker-compose.yml`: PostgreSQL database service

## 1. Start PostgreSQL

From project root:

```bash
cp .env.example .env
docker compose up -d db
```

## 2. Run Backend (FastAPI)

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload --port 8000
```

## 3. Run Frontend (Next.js)

In a new terminal:

```bash
cd frontend
npm install
cp .env.local.example .env.local
npm run dev
```

App URLs:

- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API docs: http://localhost:8000/docs

## Current Features

- Create and list government projects
- Track budget allocated and spent
- Record project status and implementation ownership
- Milestone API endpoints for project progress tracking

## Suggested Next Steps

- Add authentication and role-based access control
- Add media evidence uploads and audit logs
- Add public scorecards and downloadable reports
- Add alerts for delayed projects and budget overruns
