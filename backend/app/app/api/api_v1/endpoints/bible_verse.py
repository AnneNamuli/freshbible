from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.post("/chapter/verse", response_model=schemas.BibleVerse)
def create_bible_verse(
    *,
    db: Session = Depends(deps.get_db),
    verse_in: schemas.BibleVerseCreate,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Create new verse of the bible.
    """
    verse = crud.verse.create(db, obj_in=verse_in)
    return verse


@router.get("/chapter/verse/{id}", response_model=schemas.BibleVerse)
def read_verse_by_id(
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Read verse by id.
    """
    verse = crud.verse.get(db, id=id)
    return verse


@router.get("/chapter/verse/{id}", response_model=schemas.BibleVerse)
def read_verse_by_id(
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Read verse by id.
    """
    verse = crud.verse.get(db, id=id)
    return verse


@router.get("/chapter/verse", response_model=List[schemas.BibleVerse])
def read_bible_verses(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Retrieve all verses of the bible.
    """
    chapter = crud.verse.get_multi(db, skip=skip, limit=limit)
    return chapter
