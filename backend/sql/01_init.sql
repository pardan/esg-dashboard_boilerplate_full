CREATE EXTENSION IF NOT EXISTS timescaledb;

CREATE TABLE sensor_data (
    id SERIAL,
    time TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    device_id TEXT NOT NULL,
    metric_type TEXT NOT NULL,
    value DOUBLE PRECISION NOT NULL,
    PRIMARY KEY (time, id)
);

SELECT create_hypertable('sensor_data', 'time');
