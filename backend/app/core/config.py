from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Faraja API"
    app_version: str = "0.1.0"
    database_url: str = Field(
        default="postgresql+psycopg://postgres:postgres@localhost:5432/faraja"
    )
    frontend_origin: str = "http://localhost:3000,http://127.0.0.1:3001,http://localhost:3001,http://127.0.0.1:3001"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    @field_validator("frontend_origin")
    @classmethod
    def normalize_frontend_origin(cls, value: str) -> str:
        return value.strip()


settings = Settings()
