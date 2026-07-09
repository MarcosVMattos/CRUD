from fastapi import HTTPException

from storage import cont_id, tasks
from schemas import TaskCreate, TaskId, TaskUpdate

def create_task(task: TaskCreate):
    global cont_id
    cont_id += 1
    task_id = TaskId(id=cont_id, title=task.title, description=task.description)
    tasks.append(task_id)
    return task_id

def get_all_tasks():
    return tasks

def get_task_by_id(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(
        status_code=404,
        detail= "Tarefa não encontrada"
    )

def update_task(task_id: int, data: TaskUpdate):
    task = get_task_by_id(task_id)
    if task:
        if data.title is not None:
            if data.title.strip() != "":
                task.title = data.title
            else:
                raise HTTPException(status_code=400,
                                    detail="O campo title não pode ficar vazio")
        if data.description is not None:
            task.description = data.description
    return task

def delete_task(task_id: int):
    task = get_task_by_id(task_id)
    tasks.remove(task)
    return
