
from fastapi import FastAPI
import httpx

app = FastAPI()

@app.get("/joke")
async def get_joke():
    url = "https://official-joke-api.appspot.com/random_joke"

    async with httpx.AsyncClient() as client:
        res = await client.get(url)

    if res.status_code == 200:
        data = res.json()
        return {}