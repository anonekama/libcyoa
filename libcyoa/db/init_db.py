import logging
from sqlalchemy.orm import Session

from libcyoa import crud, schemas
from libcyoa.db import base  # noqa: F401

logger = logging.getLogger(__name__)

FIRST_SUPERUSER = "admin"

LINKS = [
    {
        "id": 1,
        "title": "Chicken Vesuvio 1234",
        "host": "Serious Eats",
        "url": "http://www.seriouseats.com/recipes/2011/12/chicken-vesuvio-recipe.html",
    },
    {
        "id": 2,
        "title": "Chicken Paprikash 541",
        "host": "No Recipes",
        "url": "http://norecipes.com/recipe/chicken-paprikash/",
    },
    {
        "id": 3,
        "title": "Cauliflower and Tofu Curry Recipe 532",
        "host": "Serious Eats",
        "url": "http://www.seriouseats.com/recipes/2011/02/cauliflower-and-tofu-curry-recipe.html",
    },
]

# make sure all SQL Alchemy models are imported (app.db.base) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28


def init_db(db: Session) -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next line
    # Base.metadata.create_all(bind=engine)
    if FIRST_SUPERUSER:
        user = crud.user.get_by_username(db, username=FIRST_SUPERUSER)
        if not user:
            user_in = schemas.UserCreate(
                username=FIRST_SUPERUSER,
                is_superuser=True,
            )
            user = crud.user.create(db, obj_in=user_in)  # noqa: F841
        else:
            logger.warning(
                "Skipping creating superuser. User with username "
                f"{FIRST_SUPERUSER} already exists. "
            )
        if not user.links:
            for link in LINKS:
                link_in = schemas.LinkCreate(
                    title=link["title"],
                    host=link["host"],
                    url=link["url"],
                    submitter_id=user.id,
                )
                crud.link.create(db, obj_in=link_in)
    else:
        logger.warning(
            "Skipping creating superuser.  FIRST_SUPERUSER needs to be "
            "provided as an env variable. "
            "e.g.  FIRST_SUPERUSER=admin@api.coursemaker.io"
        )