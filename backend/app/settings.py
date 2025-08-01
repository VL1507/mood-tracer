from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel


class JWT(BaseModel):
    SECRET_KEY: str


class DB(BaseModel):
    # USER: str
    # PASSWORD: str
    # HOST: str
    # PORT: int
    # NAME: str

    URL: str


class Settings(BaseSettings):
    JWT: JWT
    DB: DB

    model_config = SettingsConfigDict(env_file="./.env", env_nested_delimiter="__")


settings = Settings()  # type: ignore
