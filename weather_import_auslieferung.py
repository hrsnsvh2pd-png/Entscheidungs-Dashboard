#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import requests
import sqlite3
from datetime import datetime, timedelta
import certifi
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# -----------------------------
# CONFIG
# -----------------------------
LAT = NN.NNNN
LON = N.NNNN
BASE_DIR = "/volume1/docker/entscheidungs_dashboard"
DB_FILE = os.path.join(BASE_DIR, "db", "entscheidungs_dashboard.db")
HOURS_FORECAST = 48

# -----------------------------
# Setup
# -----------------------------
os.makedirs(os.path.dirname(DB_FILE), exist_ok=True)

# -----------------------------
# Open-Meteo API
# -----------------------------
ENDPOINT = (
    f"https://api.open-meteo.com/v1/forecast?"
    f"latitude={LAT}&longitude={LON}"
    f"&hourly=temperature_2m,shortwave_radiation,wind_speed_10m"
    f"&timezone=Europe/Berlin"
)

session = requests.Session()
retry = Retry(
    total=5,
    connect=5,
    read=5,
    backoff_factor=1,
    status_forcelist=[500, 502, 503, 504],
)
adapter = HTTPAdapter(max_retries=retry)
session.mount("https://", adapter)

resp = session.get(ENDPOINT, timeout=30, verify=certifi.where())

if resp.status_code != 200:
    print(f"ERROR: API request failed with status {resp.status_code}")
    exit(1)

data = resp.json()

times = data["hourly"]["time"]
temps = data["hourly"]["temperature_2m"]
rads  = data["hourly"]["shortwave_radiation"]
winds = data["hourly"]["wind_speed_10m"]

# -----------------------------
# DB
# -----------------------------
conn = sqlite3.connect(DB_FILE)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS weather_forecast (
    timestamp TEXT PRIMARY KEY,
    temp_now REAL,
    temp_3h REAL,
    temp_6h REAL,
    temp_12h REAL,
    radiation REAL,
    wind_now REAL,
    wind_6h REAL,
    wind_12h REAL
)
""")

# -----------------------------
# Cleanup
# -----------------------------
now = datetime.now()
cur.execute("DELETE FROM weather_forecast WHERE timestamp < ?", (now.isoformat(),))
conn.commit()

# -----------------------------
# Insert forecast
# -----------------------------
for i, ts_str in enumerate(times):
    ts = datetime.fromisoformat(ts_str)

    if ts > now + timedelta(hours=HOURS_FORECAST):
        break

    temp_now = temps[i]

    # Temperatur-Trends
    temp_3h  = temps[i+3]  if i+3 < len(temps)  else temp_now
    temp_6h  = temps[i+6]  if i+6 < len(temps)  else temp_now
    temp_12h = temps[i+12] if i+12 < len(temps) else temp_now

    rad_v = rads[i] if i < len(rads) else 0.0

    # -----------------------------
    # WIND (3 Ebenen)
    # -----------------------------
    wind_now = winds[i] if i < len(winds) else 0.0

    wind_6h = (
        sum(winds[i:i+6]) / 6
        if i+5 < len(winds)
        else wind_now
    )

    wind_12h = (
        sum(winds[i:i+12]) / 12
        if i+11 < len(winds)
        else wind_6h
    )

    # -----------------------------
    # INSERT
    # -----------------------------
    cur.execute("""
        INSERT OR REPLACE INTO weather_forecast
        (timestamp, temp_now, temp_3h, temp_6h, temp_12h,
         radiation, wind_now, wind_6h, wind_12h)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        ts_str,
        temp_now,
        temp_3h,
        temp_6h,
        temp_12h,
        rad_v,
        wind_now,
        wind_6h,
        wind_12h
    ))

conn.commit()
conn.close()

print(f"OK: imported forecast for next {HOURS_FORECAST} hours")