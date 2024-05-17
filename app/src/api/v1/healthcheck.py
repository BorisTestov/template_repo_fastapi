from http import HTTPStatus

from fastapi import APIRouter
from models.healthcheck import HealthCheck

router = APIRouter()


@router.get(
    "",
    summary="Perform a Health Check",
    status_code=HTTPStatus.OK,
    response_model=HealthCheck,
)
async def get_health() -> HealthCheck:
    return HealthCheck(status="OK")
