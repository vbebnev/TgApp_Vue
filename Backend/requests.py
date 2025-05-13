from sqlalchemy import select, update, delete, func
from pydantic import BaseModel,ConfigDict
from typing import List
from models import async_session, User, Task

class TaskSchema(BaseModel):
    id:int
    title:str
    completed:bool
    user:int

    model_config = ConfigDict(from_attributes=True)

    

async def add_user(tg_id:int)->User:
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id==tg_id))
        if user:
            return user
        
        new_user=User(tg_id=tg_id)
        session.add(new_user)
        await session.commit()
        await session.refresh(new_user)
        return new_user

async def get_tasks(user_id:int, status:bool=False):
    async with async_session as session:
        tasks = await session.scalars(select(Task).where(Task.user==user_id, Task.completed==status))

        serialized_tasks = [
            TaskSchema.model_validate(t).model_dump for t in tasks
            
        ]

        return serialized_tasks
    
async def get_completed_tasks_count(user_id:int):
    async with async_session as session:
        cnt = await session.scalar(select(func.count(Task.id)).where(Task.user==user_id, Task.completed==True))
        return cnt
    
async def add_task(user_id:int, task_title:str):
    async with async_session as session:
        new_task = Task(user = user_id, title = task_title)
        session.add(new_task)
        await session.commit()
    
async def complete_task(task_id:int):
    async with async_session as session:
        await session.execute(update(Task).where(Task.id == task_id).value(completed = True))
        await session.complete()