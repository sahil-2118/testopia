from pydantic import BaseModel
from enum import Enum



class TaskSchemaStatusEnum(str, Enum):
    todo = "todo"
    doing = "doing"
    done = "done"


class CreateTaskReuestSchema(BaseModel):
    id : int
    title : str
    description : str | None = None

    class Config:
        from_attributes = True

class CreateTaskResponseSchema(BaseModel):
    id : int

    class Config:
        from_attributes = True


class GetTaskResponseSchema(BaseModel):
    id : int
    title : str
    description : str | None = None
    status : Enum | None = "todo"

    class Config:
        from_attributes = True

class UpdateTaskRequestSchema(BaseModel):
    title : str
    description : str | None = None
    status : Enum | None = "todo"

    class Config:
        from_attributes = True
