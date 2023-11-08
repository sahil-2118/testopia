from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .model import TaskModel
from typing import Dict, List
from ..task.schema import GetTaskResponseSchema
from database import get_db

task_router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
)

@task_router.get('/', response_model=Dict[str, List[GetTaskResponseSchema]])
async def get_task_list(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(TaskModel).offset(skip).limit(limit).all()

@task_router.get('/{task_id}', response_model=Dict[str, GetTaskResponseSchema])
async def get_task(task_id : int, db: Session = Depends(get_db)):
    return db.query(TaskModel).filter(TaskModel.id == task_id).first()

@task_router.post('/')
async def create_task():
    return {"message": "not implemented"}

@task_router.patch('/{task_id}/{status}')
async def update_task(task_id : int, status : str):
    return {"message": "not implemented"}

@task_router.delete('/{task_id}')
async def delete_task(task_id : int):
    return {"message": "not implemented"}