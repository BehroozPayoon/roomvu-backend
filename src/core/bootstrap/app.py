from fastapi import FastAPI

from src.core.settings import get_settings
from src.core.db import redis
from .routers import init_routers


def create_app() -> FastAPI:
    app_ = FastAPI(
        title=get_settings().app_name,
        description=get_settings().app_description,
        version=get_settings().version,
        docs_url="/docs",
        redoc_url="/redoc",
    )

    app_.dependency_overrides.setdefault(*redis.override_session)

    init_routers(app_=app_)

    return app_
