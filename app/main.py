from fastapi import FastAPI
from app.api.db import metadata, engine, database
from app.api.tasks import tasks

metadata.create_all(engine)

app = FastAPI()



@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(tasks)






