from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel, Field

from app.models.project import ProjectStatus


class ProjectCreate(BaseModel):
    name: str
    description: str
    county: str
    constituency: Optional[str] = None
    budget_allocated: float = Field(ge=0)
    budget_spent: float = Field(default=0, ge=0)
    start_date: date
    target_end_date: date
    status: ProjectStatus = ProjectStatus.planned
    implementing_agency: str
    lead_politician: str


class ProjectUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    county: Optional[str] = None
    constituency: Optional[str] = None
    budget_allocated: Optional[float] = Field(default=None, ge=0)
    budget_spent: Optional[float] = Field(default=None, ge=0)
    start_date: Optional[date] = None
    target_end_date: Optional[date] = None
    status: Optional[ProjectStatus] = None
    implementing_agency: Optional[str] = None
    lead_politician: Optional[str] = None


class ProjectRead(BaseModel):
    id: int
    name: str
    description: str
    county: str
    constituency: Optional[str]
    budget_allocated: float
    budget_spent: float
    start_date: date
    target_end_date: date
    status: ProjectStatus
    implementing_agency: str
    lead_politician: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
