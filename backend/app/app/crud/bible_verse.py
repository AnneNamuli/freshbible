from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from typing import List

from app.crud.base import CRUDBase
from app.models.db_models import Bible_Verse
from app.schemas.bible_verse import BibleVerseUpdate, BibleVerseCreate


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


verse = CRUDUser(Bible_Verse)
