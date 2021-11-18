from typing import Optional

from pydantic import BaseModel
from datetime import datetime

# Shared properties


class OrganizationBase(BaseModel):
    name: Optional[str] = None
    created_at: Optional[datetime] = None


# Properties to receive via API on creation
class OrganizationCreate(OrganizationBase):
    name: str


# Properties to receive via API on update
class OrganizationUpdate(OrganizationBase):
    pass


class OrganizationInDBBase(OrganizationBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class Organization(OrganizationInDBBase):
    pass


# Additional properties stored in DB
class OrganizationInDB(OrganizationInDBBase):
    pass
