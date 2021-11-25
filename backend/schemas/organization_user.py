from typing import Optional

from pydantic import BaseModel
from datetime import datetime

# Shared properties


class OrganizationUserBase(BaseModel):
    user_id: Optional[int] = None
    organization_id: Optional[int] = None
    created_at: Optional[datetime] = None

# Properties to receive via API on creation


class OrganizationUserCreate(OrganizationUserBase):
    user_id: int
    organization_id: int


# Properties to receive via API on update
class OrganizationUserUpdate(OrganizationUserBase):
    pass


class OrganizationUserInDBBase(OrganizationUserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class OrganizationUser(OrganizationUserInDBBase):
    pass


# Additional properties stored in DB
class OrganizationUserInDB(OrganizationUserInDBBase):
    pass
