from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.db.models import User
from app.schemas.user import UserCreate,UserLogin
from app.core.security import hash_password,verify_password,create_access_token
from fastapi import HTTPException, status

class UserService:
    async def create_user(self, db: AsyncSession, payload: UserCreate) -> User:
        user = User(**payload.dict())
        hashed = hash_password(user.password)
        user.password = hashed
        db.add(user)
        await db.commit()
        await db.refresh(user)
        return user
    
    async def validate_user(self, db: AsyncSession, payload: UserLogin):
        stmt = select(User).where(User.email == payload.email)
        result = await db.execute(stmt)
        user = result.scalar_one_or_none()

        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

        if not verify_password(payload.password, user.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid password"
            )

        token = create_access_token({"sub": str(user.id)})

        return {
            "success": True,
            "message": "Login successful",
            "data": {
                "access_token": token,
                "token_type": "bearer",
                "user": {
                    "id": user.id,
                    "email": user.email,
                    "name": user.name,
                }
            }
        }

    async def list_users(self, db: AsyncSession):
        result = await db.execute(select(User))
        return result.scalars().all()