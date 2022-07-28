from app.api.models import Task
from app.api.db import tasks, database

async def add_task(payload: Task):
    query=tasks.insert().values(**payload.dict())
    return await database.execute(query=query)

async def get_tasks():
    query=tasks.select()
    return await database.fetch_all(query=query)

async def get_task(sid:str):
    query=tasks.select().where(tasks.c.task_uuid==sid)
    return await database.fetch_one(query=query)

async def update_task(sid:str, payload:Task):
    query=(
        tasks
        .update()
        .where(tasks.c.task_uuid==sid)
        .values(**payload.dict())
    )
    return await database.fetch_one(query=query)