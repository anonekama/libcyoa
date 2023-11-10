from libcyoa.crud.base import CRUDBase
from libcyoa.models.link import Link
from libcyoa.schemas.link import LinkCreate, LinkUpdate


class CRUDLink(CRUDBase[Link, LinkCreate, LinkUpdate]):
    ...

link = CRUDLink(Link)