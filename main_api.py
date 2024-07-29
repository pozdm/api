import uvicorn
from fastapi import FastAPI

from api.statistics_api import router as statistics_router

app = FastAPI()
app.include_router(statistics_router)
