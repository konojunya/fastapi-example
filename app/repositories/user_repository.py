from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.models.user import User

class UserRepository:
    def create(self, db: Session, *, name: str, email: str) -> User:
        user = User(name=name, email=email)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    def list(self, db: Session) -> list[User]:
        stmt = select(User).order_by(User.id.asc())
        result = db.execute(stmt)
        return list(result.scalars().all())

    def get(self, db: Session, *, email: str) -> User | None:
        stmt = select(User).where(User.email == email)
        result = db.execute(stmt)
        return result.scalar_one_or_none()