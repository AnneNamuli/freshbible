from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend import crud, models, schemas
from backend.api import deps

router = APIRouter()


@router.post("/", response_model=schemas.BibleVerse)
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


@router.get("/{id}", response_model=schemas.BibleVerse)
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


@router.get("/", response_model=List[schemas.BibleVerse])
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


@router.get("/chapter/{chapter}", response_model=List[schemas.BibleVerse])
def read_bible_verses_by_chapter(
    chapter: str,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Search specific chapter of the bible
    """
    chapter = crud.verse.get_chapter(
        db, chapter=chapter, skip=skip, limit=limit)
    return chapter


@router.get("/{chapter}/{start}-{end}", response_model=List[schemas.BibleVerse])
def read_bible_verse_range(
    chapter: str,
    start: int,
    end: int,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Search verse range from the bible
    """
    chapter = crud.verse.get_verse_range(
        db, chapter=chapter, start=start, end=end)
    return chapter


@router.get("/{chapter}/verse/{verse_number}", response_model=schemas.BibleVerse)
def read_bible_verse(
    chapter: str,
    verse_number: int,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Search specific verse bible
    """
    chapter = crud.verse.get_verse(
        db, chapter=chapter, verse_number=verse_number)
    return chapter
