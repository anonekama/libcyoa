from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Any, Optional

from libcyoa import crud
from libcyoa.api import deps
from libcyoa.schemas.link import Link, LinkCreate

router = APIRouter()

@router.get("/{link_id}", status_code=200, response_model=Link)
def fetch_link(
    *,
    link_id: int,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Fetch a single link by ID
    """
    result = crud.link.get(db=db, id=link_id)
    if not result:
        # the exception is raised, not returned - you will get a validation
        # error otherwise.
        raise HTTPException(
            status_code=404, detail=f"Link with ID {link_id} not found"
        )

    return result

@router.post("/", status_code=201, response_model=Link)
def create_link(
    *, link_in: LinkCreate, db: Session = Depends(deps.get_db)
) -> dict:
    """
    Create a new link in the database.
    """
    link = crud.link.create(db=db, obj_in=link_in)

    return link