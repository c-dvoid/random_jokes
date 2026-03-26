
import httpx

async def fetch_joke():
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                "https://official-joke-api.appspot.com/random_joke"
            )
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        raise Exception(f"API вернул ошибку: {e.response.status_code}")
    except httpx.RequestError as e:
        raise Exception(f"Ошибка соединения: {e}")