


from sqlalchemy import (Table, Column, String, MetaData, create_engine, PickleType)

from databases import Database

import os


DATABASE_URI=os.getenv('DATABASE_URI')

engine=create_engine(DATABASE_URI)

metadata=MetaData()

tasks=Table(
    'tasks',
    metadata,
    Column('task_uuid', String(255), primary_key=True),
    Column('description', String(255)),
    Column('params', PickleType)
)

database=Database(DATABASE_URI)
