from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    name: str
    password:str
    status:bool

class UserLogin(BaseModel):
    email:str
    password:str

class UserOut(BaseModel):
    id: int
    email: str
    name: str
    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    id: int
    email: str
    name: str

class LoginResponse(BaseModel):
    success: bool
    message: str
    data: dict