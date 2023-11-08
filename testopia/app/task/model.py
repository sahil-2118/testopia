from sqlalchemy import Enum, Column, DateTime, Integer, String
import enum
from database import Base
from datetime import datetime
from sqlalchemy.orm import Session
from ..task import schema

class TaskModel(Base):
    __tablename__ = "tasks"

    class TaskModelStatusEnum(enum.Enum):
        todo  = "todo"
        doing = "doing"
        done  = "done"

    id          = Column(Integer, primary_key=True, index=True)
    title       = Column(String, unique=True, index=True)
    description = Column(String)
    status      = Column(Enum(TaskModelStatusEnum))
    created_at  = Column(DateTime, default=datetime.now)
    updated_at  = Column(DateTime, default=datetime.now)
    deleted_at  = Column(DateTime)



def get_task(db: Session, task_id: int):
    return db.query(TaskModel).filter(TaskModel.id == task_id).first()



def get_tasks(db: Session, skip: int = 0, limit: int = 10):
    return db.query(TaskModel).offset(skip).limit(limit).all()


def create_task(db: Session, task: schema.CreateTaskReuestSchema):
    __default_task_status = "todo"
    db_task = TaskModel(title=task.title, description=task.description, status = __default_task_status)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def update_task(db: Session, task: schema.UpdateTaskRequestSchema):
    db_task = TaskModel(title= task.title, description= task.description, status= task.status)
    


