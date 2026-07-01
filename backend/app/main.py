from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.milestones import router as milestones_router
from app.api.projects import router as projects_router
from app.core.config import settings
from app.db.session import create_db_and_tables


app = FastAPI(title=settings.app_name, version=settings.app_version)

allowed_origins = [
    origin.strip()
    for origin in settings.frontend_origin.split(",")
    if origin.strip()
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup() -> None:
    create_db_and_tables()


@app.get("/health")
def health_check():
    return {"status": "ok"}


app.include_router(projects_router)
app.include_router(milestones_router)
