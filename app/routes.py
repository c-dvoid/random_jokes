
from fastapi import APIRouter, HTTPException
import httpx
import json
from fastapi_cache import FastAPICache
from fastapi_cache.decorator import cache

from .models import JokeResponse

router = APIRouter()

joke_cnt = 1

@router.get("/joke", response_model=JokeResponse)
async def get_joke():

    global joke_cnt

    url = "https://official-joke-api.appspot.com/random_joke"
    async with httpx.AsyncClient() as client:
        try:
            res = await client.get(url)
            res.raise_for_status()
        except httpx.HTTPError:
            raise HTTPException(status_code=502, detail="Failed to fetch joke from API")
        
    data = res.json()
    joke_id = joke_cnt
    joke_cnt += 1

    joke = JokeResponse(
        id=joke_id,
        setup=data.get("setup"),
        punchline=data.get("punchline")
        )
    
    cache_backend = FastAPICache.get_backend()
    await cache_backend.set(
        f"joke:{joke_id}",
        json.dumps(joke.dict()).encode("utf-8"),
        expire=30
    )
    
    return joke

