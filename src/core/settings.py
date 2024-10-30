from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Roomvu Test"
    app_description: str = "Roomvu Test Description"
    version: str = "1.0.0"
    level: str = ""

    redis_host: str = ""
    redis_password: str = ""


@lru_cache()
def get_settings():
    return Settings()
