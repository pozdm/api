import uvicorn
from fastapi import FastAPI
import asyncio

from utils import subscribers_stats, views_stats
from api.statistics_api import router as statistics_router

app = FastAPI()
app.include_router(statistics_router)


@app.get("/subscriptions_to_notifications/")
async def get_period_subscriptions_stat(date: str):
    res = await views_stats.get_views_by_services(date)
    return {
        "value": res
    }


if __name__ == "__main__":
    uvicorn.run("main_api:app", reload=True)
