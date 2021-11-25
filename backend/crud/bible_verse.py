from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from typing import List, Optional

from crud.base import CRUDBase
from models.db_models import Bible_Verse
from schemas.bible_verse import BibleVerseUpdate, BibleVerseCreate


class CRUDUser(CRUDBase[Bible_Verse, BibleVerseCreate, BibleVerseUpdate]):

    def create(self, db: Session, *, obj_in: BibleVerseCreate) -> Bible_Verse:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi(
        self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> List[Bible_Verse]:
        return (
            db.query(self.model)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_chapter(
        self, db: Session, *, chapter: str, skip: int = 0, limit: int = 100
    ) -> List[Bible_Verse]:
        return (
            db.query(self.model)
            .filter(self.model.chapter.ilike(chapter))
            .order_by(self.model.verse_number.asc())
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_verse_range(
        self, db: Session, *, chapter: str, start: int, end: int
    ) -> List[Bible_Verse]:
        return (
            db.query(self.model)
            .filter(self.model.chapter.ilike(chapter))
            .filter(self.model.verse_number.between(start, end))
            .order_by(self.model.verse_number.asc())
            .all()
        )

    def get_verse(
            self, db: Session, *, chapter: str, verse_number: int
    ) -> Optional[Bible_Verse]:
        return (
            db.query(self.model)
            .filter(self.model.chapter.ilike(chapter))
            .filter(self.model.verse_number == verse_number)
            .first()
        )


verse = CRUDUser(Bible_Verse)
