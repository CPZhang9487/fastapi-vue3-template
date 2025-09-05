from fastapi import FastAPI
from backend.lifespan import lifespan

app = FastAPI(lifespan=lifespan)
