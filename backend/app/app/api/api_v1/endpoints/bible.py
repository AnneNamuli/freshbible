from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from datetime import date

from app import crud, models, schemas
from app.api import deps
from app.core.config import settings

router = APIRouter()


@router.get("/", response_model=List[schemas.BibleBook])
def read_bible_books(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Retrieve books of the bible.
    """
    book = crud.bible_book.get_multi(db, skip=skip, limit=limit)
    return book


@router.post("/", response_model=schemas.BibleBook)
def create_bible_book(
    *,
    db: Session = Depends(deps.get_db),
    book_in: schemas.BibleBookCreate,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Create new book of the bible.
    """
    book = crud.bible_book.get_by_name(db, title=book_in.title)
    if book:
        raise HTTPException(
            status_code=400,
            detail="The bible book with this title already exists in the system.",
        )
    book = crud.bible_book.create(db, obj_in=book_in)
    return book
