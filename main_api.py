import uvicorn
from fastapi import FastAPI

from api.statistics_api import router as statistics_router

app = FastAPI()
app.include_router(statistics_router)

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
