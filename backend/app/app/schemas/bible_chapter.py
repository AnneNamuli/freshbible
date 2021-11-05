from typing import Optional

from sqlalchemy.sql.sqltypes import Text

from pydantic import BaseModel

# Shared properties


class BibleChapterBase(BaseModel):
    title: Optional[str] = None
    book_id: Optional[int] = None
    chapter_id: Optional[int] = None
    verse_number: Optional[int] = None
    text: Optional[Text] = None


# Properties to receive via API on creation
class BibleChapterCreate(BibleChapterBase):
    title: str
    book_id: int
    chapter_id: int
    verse_number: int
    text: Text


# Properties to receive via API on update
class BibleChapterUpdate(BibleChapterBase):
    pass


class BibleChapterInDBBase(BibleChapterBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class BibleChapter(BibleChapterInDBBase):
    pass


# Additional properties stored in DB
class BibleChapterInDB(BibleChapterInDBBase):
    pass
