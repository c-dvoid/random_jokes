
import pytest
from pydantic import ValidationError
from unittest.mock import AsyncMock, patch

from app.joke.service import get_joke


@pytest.mark.asyncio
async def test_get_joke_success():
    fake_data = {
        "setup": "Why do programmers prefer dark mode?",
        "punchline": "Because light attracts bugs."
    }

    with patch("app.joke.service.fetch_joke", new=AsyncMock(return_value=fake_data)):
        result = await get_joke()
    
    assert result.setup == fake_data["setup"]
    assert result.punchline == fake_data["punchline"]


@pytest.mark.asyncio
async def test_get_joke_invalid_response():
    fake_data = {"error": "something went wrong"}

    with patch("app.joke.service.fetch_joke", new=AsyncMock(return_value=fake_data)):
        with pytest.raises(ValidationError):
            await get_joke()