from pydantic import BaseModel
from typing import List, Optional

class GoalBase(BaseModel):
    title: str
    description: Optional[str] = None

class GoalCreate(GoalBase):
    pass

class Goal(GoalBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str
    role: str = 'user'

class User(UserBase):
    id: int
    role: str
    goals: List[Goal] = []

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None
    role: Optional[str] = None
