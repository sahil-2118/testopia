from fastapi import FastAPI
from app.task import controller

app = FastAPI()

app.include_router(controller.task_router)