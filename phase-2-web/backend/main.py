from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Task(BaseModel):
    id: int
    title: str
    completed: bool = False

tasks = []

@app.post("/tasks")
def add_task(task: Task):
    tasks.append(task)
    return {"message": "Task added", "task": task}

@app.get("/tasks")
def get_tasks():
    return tasks
