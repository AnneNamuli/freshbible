from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend import crud, models, schemas

from backend.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.OrganizationUser])
def read_organization_user(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve all organization users.
    """
    organization = crud.org_user.get_multi(db, skip=skip, limit=limit)
    return organization


@router.get("/{id}", response_model=schemas.OrganizationUser)
def read_organization_user_by_id(
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Read organization user by id.
    """
    organization = crud.org_user.get(db, id=id)
    return organization


@router.get("/user/{user_id}", response_model=List[schemas.OrganizationUser])
def read_organization_user_by_iser_id(
    user_id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Read organization user by user id.
    """
    organization = crud.org_user.get(db, id=user_id)
    return organization


@router.get("/organization/{organization_id}", response_model=List[schemas.OrganizationUser])
def read_organization_user_by_iser_id(
    organization_id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Read organization users by organization id.
    """
    organization = crud.org_user.get(db, id=organization_id)
    return organization


@router.post("/", response_model=schemas.OrganizationUser)
def create_organization_user(
    *,
    db: Session = Depends(deps.get_db),
    org_in: schemas.OrganizationUserCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new organization user.
    """
    organization = crud.org_user.create(db, obj_in=org_in)
    return organization


@router.patch("/{id}", response_model=schemas.OrganizationUser)
def update_organization_user(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    org_in: schemas.OrganizationUserUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update an organization user.
    """
    organization = crud.org_user.get(db, id=id)
    if not organization:
        raise HTTPException(
            status_code=404,
            detail="The organization user with this id does not exist in the system",
        )
    organization = crud.org_user.update(db, db_obj=organization, obj_in=org_in)
    return organization
