from datetime import date, datetime
from enum import Enum
from typing import Optional

from sqlmodel import Field, SQLModel


class ProjectStatus(str, Enum):
    planned = "planned"
    in_progress = "in_progress"
    delayed = "delayed"
    completed = "completed"
    cancelled = "cancelled"


class ProjectBase(SQLModel):
    name: str = Field(index=True)
    description: str
    county: str
    constituency: Optional[str] = None
    budget_allocated: float = Field(ge=0)
    budget_spent: float = Field(default=0, ge=0)
    start_date: date
    target_end_date: date
    status: ProjectStatus = Field(default=ProjectStatus.planned)
    implementing_agency: str
    lead_politician: str


class Project(ProjectBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
