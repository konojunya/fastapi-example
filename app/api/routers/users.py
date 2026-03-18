from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import UserService

router = APIRouter()

user_service = UserService()

@router.post("", status_code=201, response_model=UserResponse)
def create_user(payload: UserCreate, db: Session = Depends(get_db)):
    return user_service.create(db, payload)

@router.get("", status_code=200, response_model=list[UserResponse])
def list_users(db: Session = Depends(get_db)):
    return user_service.list(db)