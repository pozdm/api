import uvicorn
from fastapi import FastAPI

from utils import subscribers_stats

app = FastAPI()


@app.get("/subscriptions_to_notifications/")
async def get_period_subscriptions_stat(date):
    x, y = await subscribers_stats.subscriptions_to_notifications_period(date)
    return {"message": "я тебя люблю",
            "x": x,
            "y": y}


uvicorn.run("statistics:app", reload=True)