from pathlib import Path
import sys

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from backend.lifespan import lifespan
from backend.service.spa_support import SPA_Support

app = FastAPI(
    default_response_class=ORJSONResponse,
    lifespan=lifespan,
)

app.mount(
    "/",
    SPA_Support(
        directory=str(Path(getattr(sys, "_MEIPASS", "")) / "frontend/dist"),
    ),
    name="spa",
)
