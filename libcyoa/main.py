from fastapi import FastAPI, APIRouter, Query, HTTPException, Request, Depends
from fastapi.templating import Jinja2Templates

from typing import Optional, Any
from pathlib import Path
from sqlalchemy.orm import Session

from libcyoa.schemas.link import Link, LinkCreate
from libcyoa import deps
from libcyoa import crud


# Project Directories
ROOT = Path(__file__).resolve().parent.parent
BASE_PATH = Path(__file__).resolve().parent
TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / "templates"))

app = FastAPI(
    title="LibCYOA API", openapi_url="/openapi.json"
)

api_router = APIRouter()

@api_router.get("/", status_code=200)
def root(
    request: Request,
    db: Session = Depends(deps.get_db),
) -> dict:
    """
    Root GET
    """
    links = crud.link.get_multi(db=db, limit=10)
    return TEMPLATES.TemplateResponse(
        "index.html",
        {"request": request, "links": links},
    )

@api_router.get("/link/{link_id}", status_code=200, response_model=Link)
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

@api_router.post("/link/", status_code=201, response_model=Link)
def create_recipe(
    *, link_in: LinkCreate, db: Session = Depends(deps.get_db)
) -> dict:
    """
    Create a new recipe in the database.
    """
    link = crud.link.create(db=db, obj_in=link_in)

    return link


app.include_router(api_router)


if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")