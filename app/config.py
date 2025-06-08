from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    alphavantage_api_key: str
    database_url: str

    class Config:
        env_file = ".env"

settings = Settings()
