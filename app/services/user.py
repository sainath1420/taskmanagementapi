from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from datetime import timedelta
from app.config.utils import get_password_hash, verify_password, create_access_token
from app.crud.user import UserCrud
from app.schemas.user import UserCreate, UserResponse

ACCESS_TOKEN_EXPIRE_MINUTES = 10

class UserService:
    def __init__(self, db: Session):
        self.db = db

    def login_user(self,form_data):
        user = UserCrud(db=self.db).get_user(username=form_data.username)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )

        if not user or not verify_password(form_data.password, user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )

        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.username}, expires_delta=access_token_expires
        )

        return {"access_token": access_token, "token_type": "bearer"}

    def create_user(self, user_create: UserCreate):
        try:
            get_user = UserCrud(db=self.db).get_user(username=user_create.username)
            if get_user:
                raise HTTPException(status_code=409, detail="User Already Exists")

            hashed_password = get_password_hash(user_create.password)

            create_user = UserCrud(db=self.db).create_user(user_create=user_create, hashed_password=hashed_password)
            if not create_user:
                raise HTTPException(status_code=400, detail="User Creation Failed")

            context = "User Created Successfully"
            response = UserResponse(details=context)
            return response
        except Exception as e:
            if isinstance(e, HTTPException):
                raise e
            return {"status_code":500, "detail": e}