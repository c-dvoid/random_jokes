
from pydantic import ValidationError
import pytest
from httpx import AsyncClient, ASGITransport
from unittest.mock import AsyncMock, patch

from app.main import app
from app.joke.schemas import Joke 


@pytest.fixture(autouse=True)
def mock_redis():
    with patch("app.joke.router.redis") as mock:
        mock.incr = AsyncMock(return_value=1)
        mock.expire = AsyncMock()
        mock.ttl = AsyncMock(return_value=60)
        yield mock

@pytest.mark.asyncio
async def test_joke_endpoint_success():
    fake_joke = Joke(setup="Why dark mode?", punchline="Light attracts bugs.")

    with patch("app.joke.router.get_joke", new=AsyncMock(return_value=fake_joke)):
        async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
            response = await client.get("/joke")

    assert response.status_code == 200
    assert response.json()["setup"] == "Why dark mode?"


@pytest.mark.asyncio
async def test_joke_endpoint_bad_gateway():
    try:
        Joke(error="bad")
    except ValidationError as e:
        error = e

    with patch("app.joke.router.get_joke", new=AsyncMock(side_effect=(error))):
        async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
            response = await client.get("/joke")

    assert response.status_code == 502


@pytest.mark.asyncio
async def test_joke_endpoint_service_unavailable():
    with patch("app.joke.router.get_joke", new=AsyncMock(side_effect=Exception("connection error"))):
        async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
            response = await client.get("/joke")

        assert response.status_code == 503


@pytest.mark.asyncio
async def test_joke_endpoint_rate_limit(mock_redis):
    mock_redis.incr = AsyncMock(return_value=11)
    mock_redis.ttl = AsyncMock(return_value=30)

    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        response = await client.get("/joke")

    assert response.status_code == 429
    assert "30" in response.json()["detail"]