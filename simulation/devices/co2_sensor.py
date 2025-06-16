import random
import time
from backend.db import save_reading

class CO2Sensor:
    def __init__(self, device_id):
        self.device_id = device_id

    def read_value(self):
        # Occasionally simulate very high values
        if random.random() > 0.95:
            return 400 + random.uniform(-50, 2000)
        else:
            return 400 + random.uniform(-50, 50)

if __name__ == '__main__':
    sensor = CO2Sensor('test_device')

    while True:
        value = round(sensor.read_value(), 2)
        print(f'CO₂ Reading: {value:.2f} ppm')

        # Save to database
        save_reading(sensor.device_id, "co2", value)

        # Wait 5 seconds
        time.sleep(5)
