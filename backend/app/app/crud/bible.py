from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from typing import List

from app.crud.base import CRUDBase
from app.models.db_models import Bible_Book
from app.schemas.bible_books import BibleBookCreate, BibleBookUpdate


class CRUDUser(CRUDBase[Bible_Book, BibleBookCreate, BibleBookUpdate]):
    def get_by_name(self, db: Session, *, title: str) -> Optional[Bible_Book]:
        return db.query(Bible_Book).filter(Bible_Book.title == title).first()

    def create(self, db: Session, *, obj_in: BibleBookCreate) -> Bible_Book:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi(
        self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> List[Bible_Book]:
        return (
            db.query(self.model)
            .offset(skip)
            .limit(limit)
            .all()
        )


bible_book = CRUDUser(Bible_Book)
