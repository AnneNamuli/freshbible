from typing import Optional

from sqlalchemy.sql.sqltypes import Text

from pydantic import BaseModel

# Shared properties


class BibleVerseBase(BaseModel):
    title: Optional[str] = None
    book_id: Optional[int] = None
    chapter_id: Optional[int] = None
    verse_number: Optional[int] = None
    text: Optional[Text] = None


# Properties to receive via API on creation
class BibleVerseCreate(BibleVerseBase):
    title: str
    book_id: int
    chapter_id: int
    verse_number: int
    text: Text


# Properties to receive via API on update
class BibleVerseUpdate(BibleVerseBase):
    pass


class BibleVerseInDBBase(BibleVerseBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class BibleVerse(BibleVerseInDBBase):
    pass


# Additional properties stored in DB
class BibleVerseInDB(BibleVerseInDBBase):
    pass
