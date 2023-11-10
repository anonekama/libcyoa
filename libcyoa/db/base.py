# Import all the models, so that Base has them before being
# imported by Alembic
from libcyoa.db.base_class import Base  # noqa
from libcyoa.models.user import User  # noqa
from libcyoa.models.link import Link  # noqa