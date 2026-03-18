from fastapi import FastAPI

from app.api.routers import hello, health
from app.middleware.access_log import AccessLogMiddleware
from app.core.logging import setup_logging

setup_logging()

def create_app() -> FastAPI:
    app = FastAPI(title="FastAPI Example")

    app.add_middleware(AccessLogMiddleware)

    app.include_router(health.router)
    app.include_router(hello.router, prefix="/hello", tags=["hello"])

    return app

app = create_app()