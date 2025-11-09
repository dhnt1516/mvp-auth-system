from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    HASH_SCHEME: str = "argon2"
    SECRET_KEY: str
    APP_ENV: str = "production"
    ARGON2_TIME_COST: int = 2
    ARGON2_MEMORY_COST: int = 65536
    ARGON2_PARALLELISM: int = 2
    BACKEND_PORT: int = 8000

    class Config:
        env_file = ".env"

settings = Settings()
