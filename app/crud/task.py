from sqlalchemy import update, delete
from sqlalchemy.orm import Session
from sqlmodel import select
from app.models.task import Task
from app.schemas.task import TaskRequest, TaskUpdate


class TaskCrud:
    def __init__(self, db: Session):
        self.db = db

    def create_task(self, task_create:TaskRequest):
        statement = Task(
                        id = task_create.id,
                        title = task_create.title,
                        description = task_create.description,
                        status = task_create.status
        )
        self.db.add(statement)
        self.db.commit()
        self.db.refresh(statement)
        return statement

    def update_task(self, task_update: TaskUpdate, task_id: int):
        statement = (update(Task).values(
                            {
                                Task.title: task_update.title,
                                Task.description: task_update.description,
                                Task.status: task_update.status
                            }
                        ).where(Task.id == task_id)
                     )
        result = self.db.execute(statement)
        self.db.commit()
        return result

    def select_task(self, task_id: int):
        statement = select(Task).where(Task.id == task_id)
        result = self.db.execute(statement).first()
        return result

    def delete_task(self, task_id: int):
        statement = delete(Task).where(Task.id == task_id)
        result = self.db.execute(statement)
        self.db.commit()
        return result

    def get_all_tasks(self):
        statement = select(Task)
        result = self.db.execute(statement)
        return result.scalars().all()