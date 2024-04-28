from fastapi import FastAPI
from db.db import create_tables, get_db
from Task import router as task_router

app = FastAPI()

create_tables()

app.include_router(task_router)
