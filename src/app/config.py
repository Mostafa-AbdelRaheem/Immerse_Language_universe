# import os
# from dotenv import load_dotenv

# load_dotenv()

# DATABASE_URL = os.getenv("DATABASE_URL")
# if not DATABASE_URL:
#     raise RuntimeError(
#         "DATABASE_URL not set. Check that backend/.env exists and contains it."
#     )

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str
    VERSION: str
    API_V1_STR: str

    ###################### Postgres config #############################
    DATABASE_URL: str
    POSTGRES_PASSWORD: str


    # class Config:
    #     env_file = ".env"
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )


def get_settings():
    return Settings()