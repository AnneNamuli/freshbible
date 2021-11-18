from typing import Any, Dict, List, Union

from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from app.crud.base import CRUDBase
from app.models.db_models import Organization_User
from app.schemas.organization_user import OrganizationUserCreate, OrganizationUserUpdate


class CRUDUser(CRUDBase[Organization_User, OrganizationUserCreate, OrganizationUserUpdate]):

    def create(self, db: Session, *, obj_in: OrganizationUserCreate) -> Organization_User:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: Organization_User, obj_in: Union[OrganizationUserUpdate, Dict[str, Any]]
    ) -> Organization_User:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def get_multi(
        self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> List[Organization_User]:
        return (
            db.query(self.model)
            .offset(skip)
            .limit(limit)
            .all()
        )


org_user = CRUDUser(Organization_User)
