from contextlib import asynccontextmanager

from fastapi import FastAPI

from backend.util import uvicorn_log_override


@asynccontextmanager
async def lifespan(app: FastAPI):
    uvicorn_log_override.init()
    yield
