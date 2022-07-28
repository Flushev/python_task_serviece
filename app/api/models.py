
from pydantic import BaseModel

class Task(BaseModel):
    task_uuid: str
    description: str
    params: dict
