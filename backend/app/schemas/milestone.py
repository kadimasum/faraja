from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel

from app.models.milestone import MilestoneStatus


class MilestoneCreate(BaseModel):
    project_id: int
    title: str
    detail: Optional[str] = None
    due_date: date
    completed_date: Optional[date] = None
    status: MilestoneStatus = MilestoneStatus.not_started


class MilestoneRead(BaseModel):
    id: int
    project_id: int
    title: str
    detail: Optional[str]
    due_date: date
    completed_date: Optional[date]
    status: MilestoneStatus
    created_at: datetime

    class Config:
        from_attributes = True
