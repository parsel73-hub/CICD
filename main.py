from fastapi import FastAPI, HTTPException, Query
from datetime import datetime, timezone
from zoneinfo import ZoneInfo, available_timezones

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


@app.get("/convert")
async def convert_time(
    tz: str = Query(..., description="Целевой часовой пояс, напр. Europe/Moscow"),
    time: str = Query(None, description="Время в UTC (формат ГГ:ММ:СС). По умолчанию — сейчас"),
):
    if tz not in available_timezones():
        raise HTTPException(status_code=400, detail=f"Неизвестный часовой пояс: {tz}")

    if time:
        try:
            hours, minutes, seconds = map(int, time.split(":"))
        except ValueError:
            raise HTTPException(status_code=400, detail="Неверный формат времени. Ожидается ГГ:ММ:СС")
        utc_dt = datetime.now(timezone.utc).replace(
            hour=hours, minute=minutes, second=seconds, microsecond=0
        )
    else:
        utc_dt = datetime.now(timezone.utc)

    local_dt = utc_dt.astimezone(ZoneInfo(tz))
    return {
        "timezone": tz,
        "utc_time": utc_dt.strftime("%Y-%m-%d %H:%M:%S"),
        "local_time": local_dt.strftime("%Y-%m-%d %H:%M:%S"),
        "utc_offset": local_dt.strftime("%z"),
    }


@app.get("/convert")
async def convert_time(
    tz: str = Query(..., description="Целевой часовой пояс, напр. Europe/Moscow"),
    time: str = Query(None, description="Время в UTC (формат ЧЧ:ММ:СС). По умолчанию — сейчас"),
):
    if tz not in available_timezones():
        raise HTTPException(status_code=400, detail=f"Неизвестный часовой пояс: {tz}")

    if time:
        try:
            hours, minutes, seconds = map(int, time.split(":"))
        except ValueError:
            raise HTTPException(status_code=400, detail="Неверный формат времени. Ожидается ЧЧ:ММ:СС")
        utc_dt = datetime.now(timezone.utc).replace(
            hour=hours, minute=minutes, second=seconds, microsecond=0
        )
    else:
        utc_dt = datetime.now(timezone.utc)

    local_dt = utc_dt.astimezone(ZoneInfo(tz))
    return {
        "timezone": tz,
        "utc_time": utc_dt.strftime("%Y-%m-%d %H:%M:%S"),
        "local_time": local_dt.strftime("%Y-%m-%d %H:%M:%S"),
        "utc_offset": local_dt.strftime("%z"),
    }
