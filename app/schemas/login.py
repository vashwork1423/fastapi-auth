from pydantic import BaseModel

class LoginBase(BaseModel):
    email: str
    password: str

    class Config:
        orm_mode = True

class LoginCreate(LoginBase):
    pass

class LoginUpdate(LoginBase):
    pass

class LoginInDBBase(LoginBase):
    pass

class Login(LoginInDBBase):
    pass
