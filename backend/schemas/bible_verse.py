from typing import Optional
from pydantic import BaseModel


# Shared properties
class BibleVerseBase(BaseModel):
    chapter_id: Optional[int] = None
    verse_number: Optional[int] = None
    chapter: Optional[str] = None
    text: Optional[str] = None


# Properties to receive via API on creation
class BibleVerseCreate(BibleVerseBase):
    chapter_id: int
    verse_number: int
    chapter: str
    text: str


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
