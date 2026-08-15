from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

# Walk up from this file (src/app/config.py) to the project root, where
# .env actually lives — this makes env loading independent of CWD.
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
ENV_FILE = PROJECT_ROOT / ".env"


class Settings(BaseSettings):
    PROJECT_NAME: str
    VERSION: str
    API_V1_STR: str

    ###################### Postgres config #############################
    DATABASE_URL: str
    POSTGRES_PASSWORD: str

    model_config = SettingsConfigDict(
        env_file=ENV_FILE, env_file_encoding="utf-8", extra="ignore"
    )


def get_settings():
    return Settings()