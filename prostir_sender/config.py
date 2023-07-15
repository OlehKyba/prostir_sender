from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class TwilioSettings(BaseModel):
    account_sid: str
    auth_token: str
    from_phone: str
    attempts: int = 3


class Settings(BaseSettings):
    twilio: TwilioSettings

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="PROSTIR_",
        env_file_encoding="utf-8",
        env_nested_delimiter="__",
    )


settings = Settings()
