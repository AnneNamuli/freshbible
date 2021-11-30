from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from typing import List

from backend.crud.base import CRUDBase
from backend.models.db_models import Bible_Book
from backend.schemas.bible_books import BibleBookCreate, BibleBookUpdate


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

    def update(
        self, db: Session, *, db_obj: Bible_Book, obj_in: Union[BibleBookUpdate, Dict[str, Any]]
    ) -> Bible_Book:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)


bible_book = CRUDUser(Bible_Book)
