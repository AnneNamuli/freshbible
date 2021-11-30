from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from backend.app.app.crud import bible

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


@router.get("/{id}", response_model=schemas.BibleBook)
def read_bible_by_id(
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Read bible book by id.
    """
    book = crud.bible_book.get(db, id=id)
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


@router.patch("/{id}", response_model=schemas.BibleBook)
def update_bible_book(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    book_in: schemas.BibleBookUpdate,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Update a bible book.
    """
    bible = crud.bible_book.get_by_id(db, id=id)
    if not bible:
        raise HTTPException(
            status_code=404,
            detail="The bible book with this id does not exist in the system",
        )
    book = crud.bible_book.update_book(db, db_obj=bible, obj_in=book_in)
    return book
