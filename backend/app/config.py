
from pydantic_settings import BaseSettings
from pydantic import ConfigDict

class Settings(BaseSettings):

    model_config = ConfigDict(env_file=".env")

    redis_host: str = "redis"
    redis_port: int = 6379
    rate_limit: int = 10
    rate_limit_ttl: int = 60


settings = Settings()