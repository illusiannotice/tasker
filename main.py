from fastapi import FastAPI
from task_end.task_struct import Task
from db.crud import add_task_db, read_all, delete_task
app = FastAPI()

@app.get("/")
def main_page():
    return ...

@app.post("/add_task")
def add_task(task: Task):
    add_task_db(task)
    return {"process": "succeed"}

@app.get("/get_tasks")
def get_tasks():
    return read_all()

@app.delete("/delete_task")
def remove_task(task_name: str):
    delete_task(task_name)
    return {"process": "succeed"}
