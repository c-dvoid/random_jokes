
from pydantic import BaseModel

class JokeResponse(BaseModel):
    id: int
    setup: str
    punchline: str