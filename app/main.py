from fastapi import FastAPI

from app.api.v1.controlers import tts_router as yandex_tts_router

app = FastAPI()

app.include_router(yandex_tts_router)
