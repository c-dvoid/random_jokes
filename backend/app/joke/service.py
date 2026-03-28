
from .schemas import Joke
from .client import fetch_joke

async def get_joke() -> Joke:
    data = await fetch_joke()
    return Joke(**data)