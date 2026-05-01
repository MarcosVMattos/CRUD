from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

tasks = []
cont = 0

app = FastAPI()

@app.get("/")
def test():
    return {"message": "API funcionado"}

class Task(BaseModel):
    title: str
    description: str

class TaskId(Task):
    id: int

@app.post("/tasks", status_code=200)
def create_task(data: Task):
    global cont
    cont += 1
    task = TaskId(
        id = cont,
        title = data.title,
        description = data.description
    )
    tasks.append(task)
    return task

@app.get("/tasks", status_code=200)
def view_tasks():
    return tasks


