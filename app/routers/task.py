from fastapi import APIRouter, Depends, Path
from sqlalchemy.orm import Session

from app.config.database import get_db
from app.config.utils import get_current_user
from app.schemas.task import TaskResponse, TaskRequest, TaskUpdate, TasksResponse
from app.services.task import TaskService

router = APIRouter(
    prefix="/task",
    tags=["Task"],
    responses={404: {"description": "Not found"}},
)

@router.post("/create", response_model=TaskResponse)
async def create_task(
    task_create:TaskRequest,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
) :
    result = TaskService(db=db, user=user).create_task(task_create=task_create)
    return result

@router.put("/update/{task_id}", response_model=TaskResponse)
async def update_task(
        task_update: TaskUpdate,
        task_id: int = Path(nullable=False,description="unique id of task"),
        db: Session = Depends(get_db),
        user=Depends(get_current_user)
):
    result = TaskService(db=db, user=user).update_task(task_update=task_update, task_id=task_id)
    return result

@router.get("/getAll", response_model=TasksResponse)
async def get_all_tasks(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
) :
    result = TaskService(db=db, user=user).get_all_tasks()
    return result

@router.delete("/delete/{task_id}", response_model=TaskResponse)
async def delete_task(
        task_id: int = Path(nullable=False,description="unique id of task"),
        db: Session = Depends(get_db),
        user=Depends(get_current_user)
):
    result = TaskService(db=db, user=user).delete_task(task_id=task_id)
    return result