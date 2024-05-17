import uvicorn
from api.router import router
from core.logger import get_logger
from core.settings import app_settings
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from starlette.middleware.cors import CORSMiddleware

logger = get_logger(__name__)


def create_app():
    app = FastAPI(
        docs_url="/openapi",
        openapi_url="/openapi.json",
        default_response_class=ORJSONResponse,
        servers=[{"url": "http://127.0.0.1", "description": "Localhost"}],
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(router)

    return app


app = create_app()

if __name__ == "__main__":
    logger.info(f"Starting server on http://127.0.0.1:{app_settings.port}")
    uvicorn.run(app, host="0.0.0.0", port=app_settings.port)
