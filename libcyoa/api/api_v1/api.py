from fastapi import APIRouter

from libcyoa.api.api_v1.endpoints import link, auth


api_router = APIRouter()
api_router.include_router(link.router, prefix="/links", tags=["links"])
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])