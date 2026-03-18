import os

class Settings:
    @property
    def database_url(self) -> str:
        value = os.getenv("DATABASE_URL")
        if not value:
            raise RuntimeError("DATABASE_URL is not set")
        return value

settings = Settings()