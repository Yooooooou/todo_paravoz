from fastapi import FastAPI
from app.routers.Task import router as task_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


app.include_router(task_router)
origins = [
    "http://localhost",
    "http://localhost:8080",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)
