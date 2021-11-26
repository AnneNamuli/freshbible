from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend import crud, models, schemas

from backend.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Organization])
def read_organizations(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Retrieve all organizations.
    """
    organization = crud.organization.get_multi(db, skip=skip, limit=limit)
    return organization


@router.get("/{id}", response_model=schemas.Organization)
def read_organization_by_id(
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Read organization by id.
    """
    organization = crud.organization.get(db, id=id)
    return organization


@router.post("/", response_model=schemas.Organization)
def create_organization(
    *,
    db: Session = Depends(deps.get_db),
    org_in: schemas.OrganizationCreate,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Create new organization.
    """
    organization = crud.organization.get_by_name(db, name=org_in.name)
    if organization:
        raise HTTPException(
            status_code=400,
            detail="The organization with this name already exists in the system.",
        )
    organization = crud.organization.create(db, obj_in=org_in)
    return organization


@router.patch("/{id}", response_model=schemas.Organization)
def update_organization(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    org_in: schemas.OrganizationUpdate,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Update an organization.
    """
    organization = crud.organization.get(db, id=id)
    if not organization:
        raise HTTPException(
            status_code=404,
            detail="The organization with this id does not exist in the system",
        )
    organization = crud.organization.update(
        db, db_obj=organization, obj_in=org_in)
    return organization
