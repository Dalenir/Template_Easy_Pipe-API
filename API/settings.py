from enum import Enum
from functools import lru_cache
from typing import Any

from pydantic import BaseSettings

class AppMode(Enum):
    DEV = 'development'
    PROD = 'production'


class Settings(BaseSettings):
    API_PORT: int = 8000
    DOCKER: bool = True
    APP_MODE: AppMode = AppMode.DEV
    LOG_FILE: bool = False

    class Config:
        @classmethod
        def parse_env_var(cls, field_name: str, raw_val: str) -> Any:
            if field_name == 'APP_MODE':
                match raw_val:
                    case AppMode.DEV.value:
                        return AppMode.DEV
                    case AppMode.PROD.value:
                        return AppMode.PROD
            return cls.json_loads(raw_val)


@lru_cache()
def get_settings():
    return Settings()


main_settings = get_settings()
