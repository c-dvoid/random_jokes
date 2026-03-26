
from fastapi import APIRouter, HTTPException
from pydantic import ValidationError

from .schemas import Joke
from .service import get_joke

router = APIRouter()

@router.get("/joke", response_model=Joke)
async def joke():
    try:
        return await get_joke()
    except ValidationError:
        raise HTTPException(
            status_code=502,
            detail="Внешний API вернул неожиданный формат ответа"
        )
    except Exception as e:
        raise HTTPException(
            status_code=503,
            detail=f"Внешний API недоступен: {str(e)}"
        )