import uvicorn
from fastapi import FastAPI

from utils import subscribers_stats

app = FastAPI()


@app.get("/subscriptions_to_notifications/")
async def get_period_subscriptions_stat(start_date, end_date):
    x, y = await subscribers_stats.subscriptions_to_notifications_period(start_date, end_date)
    return {"x": x,
            "y": y}


if __name__ == "__main__":
    uvicorn.run("main_api:app", reload=True)