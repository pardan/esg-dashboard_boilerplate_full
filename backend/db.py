import os
from sqlalchemy import create_engine, text

# Path to the secrets file (relative to the backend folder)
password_file = os.path.join(os.path.dirname(__file__), '..', 'secrets', 'db_password.txt')

# Read the password from the file
with open(password_file, 'r') as f:
    db_password = f.read().strip()

# Build the connection string using the read password
engine = create_engine(f'postgresql://postgres:{db_password}@127.0.0.1:5433/postgres', pool_pre_ping=True)

def save_reading(device_id, metric, value):
    with engine.begin() as conn:
        conn.execute(text('''
            INSERT INTO sensor_data (device_id, metric_type, value)
            VALUES (:device_id, :metric, :value)
        '''), {'device_id': device_id, 'metric': metric, 'value': value})
