CREATE TABLE sensor_data (
    id SERIAL PRIMARY KEY,
    time TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    device_id VARCHAR(24) NOT NULL,
    metric_type VARCHAR(12) NOT NULL,
    value DOUBLE PRECISION NOT NULL
);
SELECT create_hypertable('sensor_data', 'time');
