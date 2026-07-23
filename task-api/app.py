from fastapi import FastAPI, HTTPException

from models import TaskCreate, TaskUpdate
import crud

app=FastAPI()

@app.get("/")
def home():
    return{
        "message":"Welcome to home."
    }

@app.get("/tasks")
def get_tasks():
    return crud.get_tasks()

@app.get("/tasks/{task_id}")
def get_task(task_id):

    task= crud.get_task(task_id)
    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"

        )
    return task

@app.post("/tasks",status_code=201)
def create_task(task:TaskCreate):

    rowid=crud.create_task(task.title)

    return{
        "id" : rowid,
        "title": task.title,
        "done":False
    }

@app.put("/tasks/{task_id}")
def update_task(task_id:int, task: TaskUpdate):

    updated=crud.update_task(
        task_id,
        task.title,
        task.done

    )

    if updated==0:
        raise HTTPException(
            status_code=404,
            detail = "task not found"
        )
    
    return {
        "message":"Task updated."
    }

@app.delete("/tasks/{task_id}")
def delete_task(task_id):

    deleted=crud.delete_task(
        task_id
    )
    if deleted == 0:
        raise HTTPException(
            status_code=404,
            detail= "Task not found"
        )
    return {
        "message":"Task deleted."
    }