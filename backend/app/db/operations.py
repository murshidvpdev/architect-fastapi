from sqlalchemy.orm import Session
from db.models import User
from schemas.user import UserCreate

class UserRepository:

    def create(self, db: Session, user: UserCreate):
        new_user = User(**user.model_dump())
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user

    def get_all(self, db: Session):
        return db.query(User).all()