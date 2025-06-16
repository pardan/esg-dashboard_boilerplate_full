from backend.db import engine
from sqlalchemy import text

def get_recent_readings(metric):
    with engine.connect() as conn:
        result = conn.execute(text('''
            SELECT value FROM sensor_data
            WHERE metric_type = :metric AND time > NOW() - INTERVAL '1 hour'
        '''), {'metric': metric})
        return [r[0] for r in result]

def send_alert(title, message):
    print(f'[ALERT] {title} - {message}')

def check_co2_levels():
    readings = get_recent_readings('co2')
    if not readings:
        return
    avg = sum(readings) / len(readings)
    if avg > 1000:
        send_alert('High CO2', f'1h Avg: {avg:.2f} ppm')

if __name__ == '__main__':
    check_co2_levels()
