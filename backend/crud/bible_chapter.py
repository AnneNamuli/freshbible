from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from typing import List

from backend.crud.base import CRUDBase
from backend.models.db_models import Bible_Chapter
from backend.schemas.bible_chapter import BibleChapterCreate, BibleChapterUpdate


class CRUDUser(CRUDBase[Bible_Chapter, BibleChapterCreate, BibleChapterUpdate]):

    def create(self, db: Session, *, obj_in: BibleChapterCreate) -> Bible_Chapter:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi(
        self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> List[Bible_Chapter]:
        return (
            db.query(self.model)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_count_chapters(
        self, db: Session, *, skip: int = 0, limit: int = 100
                           ) -> List[Bible_Chapter]:
        return (
            db.query(self.model).count()
        )


chapter = CRUDUser(Bible_Chapter)
