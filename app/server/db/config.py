from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
    database_url: PostgresDsn


def get_settings() -> Settings:
    settings = Settings()
    return settings
