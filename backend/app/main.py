from fastapi import FastAPI
from app.api.v1.routers import router as user_router
from app.db.Init_db import init_db

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    await init_db()

app.include_router(user_router, prefix="/users", tags=["Users"])