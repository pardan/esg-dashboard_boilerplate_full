from sqlalchemy import create_engine, text

engine = create_engine('postgresql://postgres:@db/postgres', pool_pre_ping=True)

def save_reading(device_id, metric, value):
    with engine.begin() as conn:
        conn.execute(text('''
            INSERT INTO sensor_data (device_id, metric_type, value)
            VALUES (:device_id, :metric, :value)
        '''), {'device_id': device_id, 'metric': metric, 'value': value})
