from pydantic import BaseSettings, AnyHttpUrl
from typing import List


class Settings(BaseSettings):
    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:8080", "http://local.liatrio.com"]'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    PROJECT_NAME: str = "Time Service"
    API_V1_STR: str = ""  # /api/v1


settings = Settings()
