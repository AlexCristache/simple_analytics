from typing import Any, Dict, List, Optional

from pydantic import BaseSettings, validator, HttpUrl, AnyHttpUrl


class Settings(BaseSettings):
    MONGO_SERVER: str
    PROJECT_NAME: str

settings = Settings()