from .user import user
from .bible import bible_book
from .bible_chapter import chapter
from .bible_verse import verse
from .organization import organization
from .organization_user import org_user

# For a new basic set of CRUD operations you could just do

# from .base import CRUDBase
# from app.models.item import Item
# from app.schemas.item import ItemCreate, ItemUpdate

# item = CRUDBase[Item, ItemCreate, ItemUpdate](Item)
