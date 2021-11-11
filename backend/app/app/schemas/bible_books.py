from typing import Optional

from pydantic import BaseModel, constr

# Shared properties


class BibleBookBase(BaseModel):
    title: Optional[str] = None
    slug: Optional[constr(max_length=3)] = None


# Properties to receive via API on creation
class BibleBookCreate(BibleBookBase):
    title: str
    slug: str


# Properties to receive via API on update
class BibleBookUpdate(BibleBookBase):
    pass


class BibleBookInDBBase(BibleBookBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class BibleBook(BibleBookInDBBase):
    pass


# Additional properties stored in DB
class BibleBookInDB(BibleBookInDBBase):
    pass
