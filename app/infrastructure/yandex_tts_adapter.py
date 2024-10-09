import io

import grpc
import pydub
from yandex.cloud.ai.tts.v3 import tts_pb2, tts_service_pb2_grpc

from app.core.config import settings
from app.domain.schemas.schemas import TTSSynthesizeRequest


class YandexTTSAdapter:
    @staticmethod
    async def synthesize(provided_data: TTSSynthesizeRequest) -> str:
        request = tts_pb2.UtteranceSynthesisRequest(
            text=provided_data.tts_text,
            output_audio_spec=tts_pb2.AudioFormatOptions(
                container_audio=tts_pb2.ContainerAudio(
                    container_audio_type=tts_pb2.ContainerAudio.WAV
                )
            ),

            hints=[
                tts_pb2.Hints(voice=provided_data.voice),
                tts_pb2.Hints(role=provided_data.role),
                tts_pb2.Hints(speed=provided_data.speed),
            ],

            loudness_normalization_type=tts_pb2.UtteranceSynthesisRequest.LUFS
        )

        cred = grpc.ssl_channel_credentials()
        channel = grpc.secure_channel('tts.api.cloud.yandex.net:443', cred)
        stub = tts_service_pb2_grpc.SynthesizerStub(channel)

        it = stub.UtteranceSynthesis(request, metadata=(
            ('authorization', f'Api-Key {settings.get_yandex_api_key}'),
        ))

        try:
            audio = io.BytesIO()
            for response in it:
                audio.write(response.audio_chunk.data)

            file_path = f"{settings.get_path_to_save_audio_files}/{provided_data.new_file_name}.wav"
            with open(file_path, 'wb') as f:
                f.write(audio.getvalue())

            return file_path

        except grpc._channel._Rendezvous as err:
            print(f'Error code {err._state.code}, message: {err._state.details}')
            raise err
