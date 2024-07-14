import uvicorn
from fastapi import FastAPI
import asyncio

from utils import subscribers_stats, views_stats
from api.statistics_api import router as statistics_router

app = FastAPI()
app.include_router(statistics_router)


if __name__ == "__main__":
    uvicorn.run("main_api:app", reload=True)
