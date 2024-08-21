import os

class Settings:
    PROJECT_NAME: str = "FastAPI Project"
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://myuser:mypassword@localhost/auth")
    PORT: int = 1234

settings = Settings()