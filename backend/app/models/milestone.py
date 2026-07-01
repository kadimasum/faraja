from datetime import date, datetime
from enum import Enum
from typing import Optional

from sqlmodel import Field, SQLModel


class MilestoneStatus(str, Enum):
    not_started = "not_started"
    in_progress = "in_progress"
    done = "done"
    blocked = "blocked"


class MilestoneBase(SQLModel):
    project_id: int = Field(foreign_key="project.id", index=True)
    title: str
    detail: Optional[str] = None
    due_date: date
    completed_date: Optional[date] = None
    status: MilestoneStatus = Field(default=MilestoneStatus.not_started)


class Milestone(MilestoneBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
