from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend import crud, models, schemas

from backend.api import deps

router = APIRouter()


@router.post("/", response_model=schemas.BibleChapter)
def create_bible_chapter(
    *,
    db: Session = Depends(deps.get_db),
    book_in: schemas.BibleChapterCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new chapter of the bible.
    """
    book = crud.chapter.create(db, obj_in=book_in)
    return book


@router.get("/{id}", response_model=schemas.BibleChapter)
def read_chapter_by_id(
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Read chapter by id(primary key).
    """
    chapter = crud.chapter.get(db, id=id)
    return chapter


@router.get("/", response_model=List[schemas.BibleChapter])
def read_bible_chapters(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve chapters of the bible.
    """
    chapter = crud.chapter.get_multi(db, skip=skip, limit=limit)
    return chapter


@router.get("/{book_id}/chapters", response_model=List[schemas.BibleChapter])
def read_chapters_by_book_id(
    book_id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Read chapter by id.
    """
    chapter = crud.chapter.get_chapters_by_book_id(db, book_id=book_id)
    return chapter
