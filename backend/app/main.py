
from fastapi import FastAPI

from app.joke.router import router

app = FastAPI()
app.include_router(router)

