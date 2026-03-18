from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate
from app.db.models.user import User

class UserService:
    def __init__(self) -> None:
        self.user_repository = UserRepository()

    def create(self, db: Session, payload: UserCreate) -> User:
        existing_user = self.user_repository.get(db, email=payload.email)
        if existing_user is not None:
            raise HTTPException(
                status_code=409,
                detail="User with this email already exists",
            )
        
        return self.user_repository.create(db, name=payload.name, email=payload.email)

    def list(self, db: Session) -> list[User]:
        return self.user_repository.list(db)