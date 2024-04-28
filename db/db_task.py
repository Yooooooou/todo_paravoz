from typing import Annotated

from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Depends
from db.models import DbTask
from schemas import Task, TaskUpdate


def create_task(db: Session, request: Task):
    new_task = DbTask(
        name=request.name,
        description=request.description,
        completed=request.completed
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


def get_task(db: Session, id: int):
    task = db.query(DbTask).filter(DbTask.id == id).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"task with id {id} not found")
    return task


def get_all_tasks(db: Session):
    all_tasks = db.query(DbTask).all()
    return all_tasks


def delete_task(db: Session, id: int):
    task = db.query(DbTask).filter(DbTask.id == id).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"task with id {id} not found")
    db.delete(task)
    db.commit()
    return {"message": "task deleted successfully"}


def delete_all_tasks(db: Session):
    db.query(DbTask).delete()
    db.commit()
    return {"message": "database cleaned"}


def update_task(db: Session, request: Annotated[TaskUpdate,Depends()], id: int):
    task = db.query(DbTask).filter(DbTask.id == id).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"task with id {id} not found")
    update_data = request.model_dump(exclude_unset=True, exclude_none=True)
    for field, value in update_data.items():
        setattr(task, field, value)

    db.commit()
    db.refresh(task)
    return task


