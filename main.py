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


@app.get("/date")
async def get_date():
    now = datetime.now(timezone.utc)
    return {
        "date": now.strftime("%Y-%m-%d"),
        "day": now.day,
        "month": now.month,
        "year": now.year,
    }


@app.get("/date/format")
async def get_date_format(fmt: str = "%Y-%m-%d"):
    now = datetime.now(timezone.utc)
    return {
        "format": fmt,
        "date": now.strftime(fmt),
    }
