# Faraja Backend (FastAPI)

## Setup

1. Ensure PostgreSQL is installed and running locally.

Ubuntu/Debian example:

```bash
sudo systemctl enable --now postgresql
sudo -u postgres psql -c "ALTER USER postgres WITH PASSWORD 'postgres';"
sudo -u postgres psql -c "CREATE DATABASE faraja OWNER postgres;"
```

2. Create virtual environment and install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

3. Copy environment variables:

```bash
cp .env.example .env
```

Default `DATABASE_URL` uses:

`postgresql+psycopg://postgres:postgres@localhost:5432/faraja`

If your local PostgreSQL credentials differ, update `DATABASE_URL` in `.env`.

4. Run API server:

```bash
uvicorn app.main:app --reload --port 8000
```

API docs are available at `http://localhost:8000/docs`.
