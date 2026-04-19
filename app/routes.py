from fastapi import APIRouter
import time
import random

router = APIRouter()

tasks = []
task_id = 0


@router.get("/")
def root():
    return {"message": "Service is running"}


@router.post("/tasks")
def create_task():
    global task_id
    task = {
        "id": task_id,
        "status": "created"
    }
    tasks.append(task)
    task_id += 1
    return task


@router.get("/tasks")
def get_tasks():
    return tasks


@router.post("/tasks/{task_id}/process")
def process_task(task_id: int):
    delay = random.uniform(0.1, 1.5)
    time.sleep(delay)

    for t in tasks:
        if t["id"] == task_id:
            t["status"] = "done"
            return {"task_id": task_id, "time": delay}

    return {"error": "task not found"}
