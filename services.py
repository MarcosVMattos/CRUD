from fastapi import HTTPException

from database import SessionLocal
from models import Task
from schemas import TaskCreate, TaskId, TaskUpdate

def create_task(data: TaskCreate):
    db = SessionLocal()
    task = Task(
        title = data.title,
        description = data.description
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    db.close()
    return task

def get_all_tasks():
    db = SessionLocal()
    tasks = db.query(Task).all()
    db.close()
    return tasks

def get_task_by_id(task_id: int):
    db = SessionLocal()
    task = db.query(Task).filter(Task.id == task_id).first()
    db.close()
    if task:
        return task
    raise HTTPException(
        status_code=404,
        detail= "Tarefa não encontrada"
    )

def update_task(task_id: int, data: TaskUpdate):
    db = SessionLocal()
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        if data.title is not None:
            task.title = data.title
        if data.description is not None:
            task.description = data.description
        db.commit()
        db.refresh(task)
        db.close()
        return task
    else:
        db.close()
        raise HTTPException(
            status_code=404,
            detail="Tarefa não encontrada"
        )

def delete_task(task_id: int):
    db = SessionLocal()
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        db.delete(task)
        db.commit()
        db.close()
        return
    else:
        db.close()
        raise HTTPException(
            status_code=404,
            detail="Tarefa não encontrada"
        )
