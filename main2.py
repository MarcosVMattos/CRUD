from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

tasks = []
cont_id = 0 

@app.get("/")
def test():
    return {"message": "API funcionado"}

class Task(BaseModel):
    title: str
    description: Optional[str]

class TaskId(Task):
    id: int

class TaskUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    
@app.post("/tasks", status_code=200)
def task(data: Task):
    if data.title.strip() == "":
        return {"message": "Required title field"}
    global cont_id
    cont_id += 1
    task = TaskId(id=cont_id, title=data.title, description=data.description)
    tasks.append(task)
    return task

@app.get("/tasks", status_code=200)
def view_tasks():
    return tasks

def search_id(id):
    for task in tasks:
        if task.id == id:
            return task
    raise HTTPException(
        status_code=404,
        detail= "Not found"
    )

@app.get("/tasks/{id}", status_code=200)
def view_task(id: int):
    return search_id(id)

@app.patch("/tasks/{id}", status_code=200)
def update_task(id: int, data: TaskUpdate):
    task = search_id(id)
    if data.title is not None:
        task.title = data.title
    if data.description is not None:
        task.description = data.description
    return task

@app.delete("/tasks/{id}", status_code=200)
def delete_task(id):
    task = search_id(id)
    tasks.remove(task)
    return {"message": f"Task {task.id} removed"}
