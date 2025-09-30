
from pydantic import BaseModel

class JokeResponse(BaseModel):
    setup: str
    punchline: str