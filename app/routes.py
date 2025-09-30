
import time

from fastapi import APIRouter, HTTPException
import httpx
from models import JokeResponse

router = APIRouter()

_cache = {"data": None, "timestamp": 0}
CASHE_DURATION = 30 # seconds

@router.get("/joke", response_model=JokeResponse)
async def get_joke():

    now = time.time()
    if _cache["data"] and now - _cache["timestamp"] < CASHE_DURATION:
        return _cache["data"]

    url = "https://official-joke-api.appspot.com/random_joke"
    async with httpx.AsyncClient() as client:
        try:
            res = await client.get(url)
            res.raise_for_status()
        except httpx.HTTPError:
            raise HTTPException(status_code=502, detail="Failed to fetch joke from API")
        
    data = res.json()
    joke = JokeResponse(setup=data.get("setup"), punchline=data.get("punchline"))
    _cache["data"] = JokeResponse(setup=data.get("setup"), punchline=data.get("punchline"))
    _cache["timestamp"] = now

    return joke