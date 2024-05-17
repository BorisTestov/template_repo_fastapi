from api.v1 import healthcheck
from fastapi import APIRouter


def create_router():
    router = APIRouter(prefix="/api/v1")
    router.include_router(
        healthcheck.router, prefix="/healthcheck", tags=["healthcheck"]
    )
    return router


router = create_router()
