from pydantic_settings import BaseSettings
from typing import List
import json


class Settings(BaseSettings):
    MONGODB_URI: str
    OPENAI_API_KEY: str
    NEXTAUTH_SECRET: str
    ENVIRONMENT: str = "development"
    BACKEND_CORS_ORIGINS: str = '["http://localhost:3000"]'

    @property
    def cors_origins(self) -> List[str]:
        return json.loads(self.BACKEND_CORS_ORIGINS)

    class Config:
        env_file = ".env"


settings = Settings()
