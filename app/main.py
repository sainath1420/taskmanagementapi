import uvicorn
from fastapi import FastAPI

from app.config.database import init_db
from app.routers import task, auth

app = FastAPI(
    title="Task Management",
    description="Task Management APIs",
    version="1.0.0",
)

init_db()

app.include_router(task.router)
app.include_router(auth.router)


if __name__ =='__main__':
    uvicorn.run('main:app')