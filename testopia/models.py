from sqlalchemy import Enum, Column, DateTime, Integer, String
import enum
from .database import Base

class Task(Base):
    __tablename__ = "tasks"

    class StatusEnum(enum.Enum):
        todo = "todo"
        doing = "doing"
        done = "done"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    description = Column(String)
    status = Column(Enum(StatusEnum))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)