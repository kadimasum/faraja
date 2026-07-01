from typing import List

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlmodel import Session, select

from app.db.session import get_session
from app.models.milestone import Milestone
from app.models.project import Project
from app.schemas.milestone import MilestoneCreate, MilestoneRead


router = APIRouter(prefix="/milestones", tags=["milestones"])


@router.get("", response_model=List[MilestoneRead])
def list_milestones(
    project_id: int | None = Query(default=None),
    session: Session = Depends(get_session),
):
    query = select(Milestone)
    if project_id is not None:
        query = query.where(Milestone.project_id == project_id)
    return session.exec(query.order_by(Milestone.due_date)).all()


@router.post("", response_model=MilestoneRead, status_code=status.HTTP_201_CREATED)
def create_milestone(payload: MilestoneCreate, session: Session = Depends(get_session)):
    project = session.get(Project, payload.project_id)
    if not project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")

    milestone = Milestone(**payload.model_dump())
    session.add(milestone)
    session.commit()
    session.refresh(milestone)
    return milestone
