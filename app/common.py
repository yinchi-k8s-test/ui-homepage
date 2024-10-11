"""Common definitions required by both the FastAPI (main) and Dash (ui) modules."""

from pydantic import Field, MariaDBDsn, MySQLDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Settings for the Homepage service."""

    host: str = Field(
        default='ychyperv'
    )

    root_path: str = Field(
        default='/',
        description='Path to serve the Homepage service from.')

    db_url: MySQLDsn | MariaDBDsn = Field(
        description='Database connection string. Only MySQL and MariaDB supported.'
    )

    model_config = SettingsConfigDict(
        env_file='secret.env',
        env_file_encoding='utf-8'
    )


settings = Settings()
