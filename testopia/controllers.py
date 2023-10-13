from fastapi import FastAPI

app = FastAPI()

@app.get('api/v1/task/')
def get_task_list():
    pass

@app.get('api/v1/task/{task_id}')
def get_task(task_id : int):
    pass

@app.post('api/v1/task/')
def create_task():
    pass

@app.patch('api/v1/task/{task_id}/{status}')
def update_task(task_id : int, status : str):
    pass

@app.delete('api/v1/task/{task_id}')
def delete_task(task_id : int):
    pass