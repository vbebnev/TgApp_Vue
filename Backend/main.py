from contextlib import asynccontextmanager

from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models import init_db
import requests as rq

class AddTask(BaseModel):
    tg_id:int
    title:str

class CompleteTask(BaseModel):
    id:int

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    print ("bot is ready")
    yield


app = FastAPI(title="To do QP", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://tgtodotest.web.app"],
    allow_credentials=True,
    allow_methods="*",
    allow_header="*",
)

@app.get("/api/tasks/{tg_ig}")
async def tasks(tg_id:int):
    user = await rq.add_user(tg_id)
    return rq.get_tasks(user.id)

@app.get("/api/main/{tg_id}")
async def profile(tg_id:int):
    user = await rq.add_user(tg_id)
    completed_tasks_count = await rq.get_completed_tasks_count(user.id)
    return {'completedTasks':completed_tasks_count}

@app.post("/api/add")
async def addTask(task:AddTask):
    user = await rq.add_user(task.tg_id)
    await rq.add_task(user.id,task.title)
    return {'status': 'ok'}

@app.patch("/api/complete")
async def completeTask(task:CompleteTask):
    user = await rq.add_user(task.tg_id)
    await rq.complete_task(user.id)
    return {'status': 'ok'}
    