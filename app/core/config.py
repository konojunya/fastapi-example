import os

class Settings:
    @property
    def database_url(self) -> str:
        return os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/app_db")


settings = Settings()