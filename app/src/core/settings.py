from dotenv import find_dotenv, load_dotenv
from pydantic import Field, field_validator
from pydantic_settings import BaseSettings

load_dotenv(find_dotenv(".env"))


class LogSettings(BaseSettings):
    level: str = "INFO"

    @field_validator("level")
    @classmethod
    def check_logging_level(cls, value):
        valid_levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
        value = value.upper()
        if value not in valid_levels:
            raise ValueError(
                f"Invalid logging level: {value}. Valid levels are: {valid_levels}"
            )
        return value

    class Config:
        env_prefix = "LOG_"


class AppSettings(BaseSettings):
    port: int = Field(default=8000, ge=1, le=65535)

    class Config:
        env_prefix = "APP_"


log_settings = LogSettings()
app_settings = AppSettings()
