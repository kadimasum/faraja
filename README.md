# Faraja - Government Project Accountability Platform

Faraja is a fullstack application for tracking implementation of government projects and increasing public accountability.

## Stack

- Frontend: Next.js (TypeScript)
- Backend: FastAPI (Python)
- Database: PostgreSQL

## Project Structure

- `frontend/`: Next.js dashboard for creating and viewing projects
- `backend/`: FastAPI API with project and milestone endpoints

## 1. Start PostgreSQL (Local Installation)

Install and start PostgreSQL locally (Ubuntu/Debian):

```bash
sudo apt update
sudo apt install -y postgresql postgresql-contrib
sudo systemctl enable --now postgresql
```

Create the application database and set the password for `postgres` role:

```bash
sudo -u postgres psql -c "ALTER USER postgres WITH PASSWORD 'postgres';"
sudo -u postgres psql -c "CREATE DATABASE faraja OWNER postgres;"
```

If the database already exists, ignore the create database error.

From project root, copy base environment file:

```bash
cp .env.example .env
```

## 2. Run Backend (FastAPI)

```bash
cd backend
python3 -m venv .venv
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
npm run dev -- -p 3001
```

App URLs:

- Frontend: http://localhost:3001
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
