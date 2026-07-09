from fastapi import APIRouter

from schemas import TaskCreate, TaskId, TaskUpdate
from services import create_task, get_all_tasks, get_task_by_id, update_task, delete_task

router = APIRouter()

@router.get("/")
def root():
    return {"message": "API criada com sucesso"}

@router.post("/tasks", status_code=201, response_model=TaskId)
def create(data: TaskCreate):
    return create_task(data)

@router.get("/tasks", status_code=200, response_model=list[TaskId])
def get_tasks():
    return get_all_tasks()

@router.get("/tasks/{task_id}", status_code=200, response_model=TaskId)
def get_task(task_id: int):
    return get_task_by_id(task_id)
    
@router.patch("/tasks/{task_id}", status_code=200, response_model=TaskId)
def update(task_id: int, data: TaskUpdate):
   return update_task(task_id, data)

@router.delete("/tasks/{task_id}", status_code=204)
def delete(task_id: int):
    return delete_task(task_id)
