from pathlib import Path
from typing import Optional, Any

from fastapi import FastAPI, APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from libcyoa import crud
from libcyoa.api import deps
from libcyoa.api.api_v1.api import api_router
from libcyoa.core.config import settings

# Project Directories
BASE_PATH = Path(__file__).resolve().parent
TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / "templates"))

root_router = APIRouter()
app = FastAPI(title="LibCYOA API")

@root_router.get("/", status_code=200)
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

app.include_router(api_router, prefix=settings.API_V1_STR)
app.include_router(root_router)

if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")