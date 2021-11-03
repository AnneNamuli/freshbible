from typing import Optional

from pydantic import BaseModel, EmailStr, constr
from datetime import date, datetime


# Shared properties
class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone_number: Optional[constr(max_length=12)]
    is_active: Optional[bool] = True
    is_superuser: bool = False
    created_at: Optional[datetime] = None
    modified_at: Optional[str] = None
    date_of_birth: Optional[date] = None
    full_name: Optional[str] = None


# Properties to receive via API on creation
class UserCreate(UserBase):
    email: EmailStr
    first_name: str
    last_name: str
    phone_number: str
    date_of_birth: Optional[date]
    password: str


# Properties to receive via API on update
class UserUpdate(UserBase):
    password: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone_number: Optional[str] = None
    date_of_birth: Optional[str] = None


class UserInDBBase(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class User(UserInDBBase):
    pass


# Additional properties stored in DB
class UserInDB(UserInDBBase):
    hashed_password: str
