from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException

from app.domain.schemas.schemas import TTSSynthesizeRequest, AudioFilesURLsResponse
from app.domain.services.yandex_tts_interactor import YandexTTSInteractor

tts_router = APIRouter(
    tags=['YandexTTSSynthesize'],
    prefix='/api/v1'
)

@tts_router.post("/synthesize", response_model=AudioFilesURLsResponse)
async def synthesize_text(request: TTSSynthesizeRequest, tts_interactor: Annotated[YandexTTSInteractor, Depends()]) -> AudioFilesURLsResponse:
    try:
        result = await tts_interactor.synthesize_and_save(request)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

