from sqlalchemy.orm import Session
from sqlmodel import select

from app.models.user import User
from app.schemas.user import UserCreate


class UserCrud:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user_create:UserCreate, hashed_password:str):
        statement = User(
                        username = user_create.username,
                        hashed_password = hashed_password,
        )
        self.db.add(statement)
        self.db.commit()
        self.db.refresh(statement)
        return statement

    def get_user(self, username: str):
        statement = select(User).where(User.username == username)
        result = self.db.execute(statement).scalars().first()
        return result