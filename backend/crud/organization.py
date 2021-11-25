from typing import Any, Dict, List, Union, Optional

from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from crud.base import CRUDBase
from models.db_models import Organization
from schemas.organization import OrganizationCreate, OrganizationUpdate


class CRUDUser(CRUDBase[Organization, OrganizationCreate, OrganizationUpdate]):
    def get_by_name(self, db: Session, *, name: str) -> Optional[Organization]:
        return db.query(Organization).filter(Organization.name == name).first()

    def create(self, db: Session, *, obj_in: OrganizationCreate) -> Organization:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: Organization, obj_in: Union[OrganizationUpdate, Dict[str, Any]]
    ) -> Organization:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def get_multi(
        self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> List[Organization]:
        return (
            db.query(self.model)
            .offset(skip)
            .limit(limit)
            .all()
        )


organization = CRUDUser(Organization)
