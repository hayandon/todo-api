from typing import Optional
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

@app.exception_handler(HTTPException)
def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(status_code=exc.status_code, content={"error": exc.detail})

class Task(BaseModel):
    id: int
    title: str
    done: bool = False

class TaskCreate(BaseModel):
    title: Optional[str] = None

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    done: Optional[bool] = None

tasks = [
    Task(id=1, title="Buy milk", done=False),
    Task(id=2, title="Walk the dog", done=False),
    Task(id=3, title="Finish assignment", done=True),
]

next_id = 4

@app.get("/")
def root():
    return {
        "name": "Task API",
        "version": "1.0",
        "endpoints": ["/tasks"]
    }

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/tasks")
def get_tasks():
    return tasks

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for t in tasks:
        if t.id == task_id:
            return t
    raise HTTPException(status_code=404, detail=f"Task {task_id} not found")

@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate):
    global next_id
    if not task.title or not task.title.strip():
        raise HTTPException(status_code=400, detail="title is required")
    new_task = Task(id=next_id, title=task.title, done=False)
    tasks.append(new_task)
    next_id += 1
    return new_task

@app.put("/tasks/{task_id}")
def update_task(task_id: int, update: TaskUpdate):
    for t in tasks:
        if t.id == task_id:
            if update.title is not None:
                if not update.title.strip():
                    raise HTTPException(status_code=400, detail="title cannot be empty")
                t.title = update.title
            if update.done is not None:
                t.done = update.done
            return t
    raise HTTPException(status_code=404, detail=f"Task {task_id} not found")

@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    for t in tasks:
        if t.id == task_id:
            tasks.remove(t)
            return
    raise HTTPException(status_code=404, detail=f"Task {task_id} not found")