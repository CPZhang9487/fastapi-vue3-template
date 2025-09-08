from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from backend.lifespan import lifespan

app = FastAPI(lifespan=lifespan)

if not Path("frontend/dist").exists():
    Path("frontend/dist").mkdir(
        parents=True,
        exist_ok=True,
    )

app.mount(
    "/",
    StaticFiles(
        directory="frontend/dist",
        html=True,
    ),
    name="static",
)
