from typing import Annotated

from fastapi import Depends

from app.domain.schemas.schemas import TTSSynthesizeRequest, AudioFilesURLsResponse
from app.infrastructure.repositories.repositories import AudioFilesURLsRepository
from app.infrastructure.yandex_tts_adapter import YandexTTSAdapter


class YandexTTSInteractor:
    def __init__(self, repository: Annotated[AudioFilesURLsRepository, Depends()]):
        self.repository = repository

    async def synthesize_and_save(self, tts_request: TTSSynthesizeRequest) -> AudioFilesURLsResponse:
        file_path = await YandexTTSAdapter.synthesize(tts_request)

        data_to_save = {
            'file_name': tts_request.filename,
            'file_path': file_path
        }

        audio_file_record = await self.repository.add(data_to_save)

        return AudioFilesURLsResponse(
            id=audio_file_record.id,
            file_name=audio_file_record.file_name,
            file_path=audio_file_record.file_path
        )
