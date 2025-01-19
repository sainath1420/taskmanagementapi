from typing import Optional

from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette.requests import Request

from app.crud.task import TaskCrud
from app.models.user import User
from app.schemas.task import TaskRequest, TaskResponse, TaskUpdate, Task, TasksResponse


class TaskService:
    def __init__(self, db: Session, user: Optional[User]=None, request: Request = None):
        self.request = request
        self.headers = {}
        self.user = user
        if request is not None:
            self.headers = {
                "Content-Type": "application/json",
                "Authorization": request.headers.get("authorization"),
            }
        self.db = db

    def create_task(self, task_create: TaskRequest):
        try:
            get_task = TaskCrud(db=self.db).select_task(task_id=task_create.id)
            if get_task:
                raise HTTPException(status_code=409, detail="Task already exists")

            task_create = TaskCrud(db=self.db).create_task(task_create=task_create)
            if not task_create:
                raise HTTPException(status_code=400, detail="task creation failed")

            context = "Task Created Successfully"
            response = TaskResponse(details=context)
            return response
        except Exception as e:
            if isinstance(e, HTTPException):
                raise e
            return {"status_code":500, "detail": e}

    def update_task(self, task_update: TaskUpdate, task_id: int):
        try:
            get_task = TaskCrud(db=self.db).select_task(task_id=task_id)
            if not get_task:
                raise HTTPException(status_code=404, detail="Task Not exists")

            task_update = TaskCrud(db=self.db).update_task(task_update=task_update, task_id=task_id)
            if not task_update:
                raise HTTPException(status_code=400, detail="task update failed")

            context = "Task Updated Successfully"
            response = TaskResponse(details=context)
            return response
        except Exception as e:
            if isinstance(e, HTTPException):
                raise e
            return {"status_code": 500, "detail": e}

    def delete_task(self, task_id: int):
        try:
            get_task = TaskCrud(db=self.db).select_task(task_id=task_id)
            if not get_task:
                raise HTTPException(status_code=404, detail="Task Not exists")

            task_delete = TaskCrud(db=self.db).delete_task(task_id=task_id)
            if not task_delete:
                raise HTTPException(status_code=400, detail="task deletion failed")

            context = "Task Deleted Successfully"
            response = TaskResponse(details=context)
            return response
        except Exception as e:
            if isinstance(e, HTTPException):
                raise e
            return {"status_code": 500, "detail": e}

    def get_all_tasks(self):
        try:
            get_all_tasks = TaskCrud(db=self.db).get_all_tasks()
            if not get_all_tasks:
                raise HTTPException(status_code=400, detail="Tasks not exists")

            tasks = [Task.model_validate(task) for task in get_all_tasks]
            response = TasksResponse(tasks=tasks)
            return response

        except Exception as e:
            if isinstance(e, HTTPException):
                raise e
            raise HTTPException(status_code=500, detail=str(e))
