
import time

from fastapi import APIRouter, HTTPException
import httpx
from models import JokeResponse

router = APIRouter()

__joke_cache = {}
CASHE_DURATION = 30 # seconds

@router.get("/joke", response_model=JokeResponse)
async def get_joke():

    url = "https://official-joke-api.appspot.com/random_joke"
    async with httpx.AsyncClient() as client:
        try:
            res = await client.get(url)
            res.raise_for_status()
        except httpx.HTTPError:
            raise HTTPException(status_code=502, detail="Failed to fetch joke from API")
        
    data = res.json()
    joke_id = data.get("id")
    now = time.time()

    if joke_id in __joke_cache:
        joke, timestamp = __joke_cache[joke_id]
        if now - timestamp < CASHE_DURATION:
            return joke

    joke = JokeResponse(setup=data.get("setup"), punchline=data.get("punchline"))
    __joke_cache[joke_id] = (joke, now)
    return joke

