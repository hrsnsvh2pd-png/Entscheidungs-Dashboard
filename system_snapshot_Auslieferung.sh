#!/bin/bash

BASE_DIR="/volume1/docker/entscheidungs_dashboard"
TARGET_DB="$BASE_DIR/db/entscheidungs_dashboard.db"
SOURCE_DB="/volume1/docker/vieventlog/db/viessmann_events.db"
LOG="$BASE_DIR/skripte/logs/system_snapshot.log"

echo "---- $(date) START system_snapshot ----" >> "$LOG"

sqlite3 "$TARGET_DB" >> "$LOG" 2>&1 <<EOF

ATTACH DATABASE '$SOURCE_DB' AS src;

WITH

-- aktuelle Stunde als Stundenende (für den Datensatz)
hw AS (
    SELECT datetime(strftime('%Y-%m-%d %H:00:00', 'now','localtime')) AS ts
),

-- Kompressorstarts aggregiert pro Stunde
t AS (
    SELECT
        installation_id,
        datetime(strftime('%Y-%m-%d %H:00:00', timestamp_mez), '+1 hour') AS ts,
        SUM(CASE WHEN compressor_ein_aus = 1 THEN 1 ELSE 0 END) AS starts
    FROM src.temperature_snapshots_takte_heute
    WHERE installation_id='1234567'
      AND timestamp_mez >= datetime('now','localtime','-2 hour')
      AND timestamp_mez < datetime('now','localtime')
    GROUP BY installation_id, ts
),

-- Laufzeit aggregiert pro Stunde
s AS (
    SELECT
        installation_id,
        datetime(strftime('%Y-%m-%d %H:00:00', timestamp_mez), '+1 hour') AS ts,
        SUM(CASE WHEN compressor_active = 1 THEN COALESCE(sample_interval,0) ELSE 0 END) AS runtime_min
    FROM src.temperature_snapshots_stat
    WHERE installation_id='1234567'
      AND timestamp_mez >= datetime('now','localtime','-2 hour')
      AND timestamp_mez < datetime('now','localtime')
    GROUP BY installation_id, ts
),

-- letzter Temperaturwert der Stunde (DHW + Buffer)
temp_last AS (
    SELECT
        installation_id,
        datetime(strftime('%Y-%m-%d %H:00:00', timestamp_mez), '+1 hour') AS ts,
        dhw_temp,
        buffer_temp
    FROM (
        SELECT
            installation_id,
            timestamp_mez,
            dhw_temp,
            buffer_temp,
            ROW_NUMBER() OVER (
                PARTITION BY datetime(strftime('%Y-%m-%d %H:00:00', timestamp_mez), '+1 hour')
                ORDER BY timestamp_mez DESC
            ) AS rn
        FROM src.temperature_snapshots_stat
        WHERE installation_id='1234567'
          AND timestamp_mez >= datetime('now','localtime','-2 hour')
          AND timestamp_mez < datetime('now','localtime')
    )
    WHERE rn = 1
)

-- Datensatz schreiben
INSERT OR REPLACE INTO system_snapshot (
    timestamp_mez,
    installation_id,
    compressor_starts_1h,
    runtime_minutes_1h,
    dhw_temp,
    buffer_temp
)
SELECT
    hw.ts AS timestamp_mez,
    '1234567' AS installation_id,
    COALESCE(t.starts,0) AS compressor_starts_1h,
    COALESCE(s.runtime_min,0) AS runtime_minutes_1h,
    temp_last.dhw_temp,
    temp_last.buffer_temp
FROM hw
LEFT JOIN t ON t.ts = hw.ts AND t.installation_id='1234567'
LEFT JOIN s ON s.ts = hw.ts AND s.installation_id='1234567'
LEFT JOIN temp_last ON temp_last.ts = hw.ts AND temp_last.installation_id='1234567';

DETACH DATABASE src;

EOF

if [ $? -eq 0 ]; then
  echo "$(date) OK: snapshot updated" >> "$LOG"
else
  echo "$(date) ERROR: snapshot failed" >> "$LOG"
fi

echo "---- $(date) END system_snapshot ----" >> "$LOG"