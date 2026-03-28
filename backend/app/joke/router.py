
from fastapi import APIRouter, Request, HTTPException
from redis.asyncio import Redis
from pydantic import ValidationError

from app.config import settings
from .schemas import Joke
from .service import get_joke

router = APIRouter()
redis = Redis(
    host=settings.redis_host,
    port=settings.redis_port,
    decode_responses=True
)

async def check_rate_limit(ip: str):
    key = f"rate: {ip}"
    count = await redis.incr(key)
    if count == 1:
        await redis.expire(key, settings.rate_limit_ttl)
    if count > settings.rate_limit:
        ttl = await redis.ttl(key)
        raise HTTPException(status_code=429, detail=f"Слишком много запросов. Попробуйте через {ttl} секунд.")

@router.get("/joke", response_model=Joke)
async def joke(request: Request):
    await check_rate_limit(request.client.host)
    try:
        return await get_joke()
    except ValidationError:
        raise HTTPException(
            status_code=502,
            detail="Внешний API вернул неожиданный формат ответа"
        )
    except Exception as e:
        raise HTTPException(
            status_code=503,
            detail=f"Внешний API недоступен: {str(e)}"
        )