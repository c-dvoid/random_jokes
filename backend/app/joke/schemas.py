
from pydantic import BaseModel

class Joke(BaseModel):
    setup: str
    punchline: str