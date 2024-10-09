from fastapi import FastAPI

from app.core.config import settings

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

print(f"URL: {'postgresql' + settings.get_db_url()[18:]}")
