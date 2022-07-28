from typing import List
from fastapi import Header, APIRouter

from app.api.models import Task
from app.api import dbmanager

tasks=APIRouter()



@tasks.post('/tasks/add', status_code=201)
async def add_task(payload: Task):
    await dbmanager.add_task(payload)
    response={
        **payload.dict()
    }
    return response

@tasks.get('/tasks', response_model=List[Task])
async def get_tasks():
    return await dbmanager.get_tasks()

@tasks.get('/tasks/{sid}', response_model=Task)
async def get_task(sid):
    return await dbmanager.get_task(sid)

@tasks.put('/tasks/{sid}')
async def upgrade_task(sid:str, payload:Task):
    t = await dbmanager.get_task(sid)
    
    update_data = payload.dict(exclude_unset=True)
    
    task_in_db = Task(**t)

    updated_task = task_in_db.copy(update=update_data)

    await dbmanager.update_task(sid,updated_task)

    response={
        **payload.dict()
    }
    return response