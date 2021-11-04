from typing import Optional

from pydantic import BaseModel

# Shared properties


class BibleChapterBase(BaseModel):
    title: Optional[str] = None


# Properties to receive via API on creation
class BibleChapterCreate(BibleChapterBase):
    title: str


# Properties to receive via API on update
class BibleChapterUpdate(BibleChapterBase):
    pass


class BibleChapterInDBBase(BibleChapterBase):
    id: Optional[int] = None
    book_id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class BibleChapter(BibleChapterInDBBase):
    pass


# Additional properties stored in DB
class BibleChapterInDB(BibleChapterInDBBase):
    pass
