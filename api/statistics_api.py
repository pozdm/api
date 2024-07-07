import uvicorn
from fastapi import FastAPI

from utils import statistics

from utils import statistics

app = FastAPI()

@app.get("/subscriptions_to_notifications/")
async def get_period_subscriptions_stat(start_date, end_date):
    pass


uvicorn.run("statistics:app", reload=True)