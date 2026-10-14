from fastapi import FastAPI
from datetime import datetime, timezone

app = FastAPI(title="Time Server")


@app.get("/")
async def root():
    return {"message": "Welcome to the Time Server"}


@app.get("/time")
async def get_time():
    now = datetime.now(timezone.utc)
    return {
        "utc_time": now.strftime("%Y-%m-%d %H:%M:%S"),
        "utc_date": now.strftime("%Y-%m-%d"),
    }
