from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.db.models import User
from app.schemas.user import UserCreate

class UserService:

    async def create_user(self, db: AsyncSession, payload: UserCreate) -> User:
        user = User(**payload.dict())
        db.add(user)
        await db.commit()
        await db.refresh(user)
        return user

    async def list_users(self, db: AsyncSession):
        result = await db.execute(select(User))
        return result.scalars().all()