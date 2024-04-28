from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.db import get_db
from schemas import Task, TaskUpdate
from db.db_task import create_task, get_task, get_all_tasks, delete_task, delete_all_tasks, update_task

router = APIRouter(
    prefix='/tasks',
    tags=['tasks']
)


@router.post('/', response_model=Task)
def create(request: Annotated[Task, Depends()], db: Session = Depends(get_db)):
    return create_task(db, request)


@router.get('/{id}')
def get(id: int, db: Session = Depends(get_db)):
    return get_task(db, id)


@router.get('/')
def get_all(db: Session = Depends(get_db)):
    return get_all_tasks(db)


@router.delete('/{id}')
def delete(id: int, db: Session = Depends(get_db)):
    return delete_task(db, id)


@router.delete('/')
def delete_all(db: Session = Depends(get_db)):
    return delete_all_tasks(db)


@router.patch('/{id}', response_model=Task)
def update(id: int, request: TaskUpdate, db: Session = Depends(get_db)):
    return update_task(db, request, id)
