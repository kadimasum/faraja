# Faraja Backend (FastAPI)

## Setup

1. Create virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Copy environment variables:

```bash
cp .env.example .env
```

3. Run API server:

```bash
uvicorn app.main:app --reload --port 8000
```

API docs are available at `http://localhost:8000/docs`.
