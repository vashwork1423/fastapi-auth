from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    email: str
    email: str
    password: str

    class Config:
        orm_mode = True

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class UserInDBBase(UserBase):
    id: int

    class Config:
        from_attributes = True

class User(UserInDBBase):
    pass
