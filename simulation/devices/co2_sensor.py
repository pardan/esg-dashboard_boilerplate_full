import random, time

class CO2Sensor:
    def __init__(self, device_id): self.device_id = device_id
    def read_value(self):
        return 400 + random.uniform(-50, 2000 if random.random() > 0.95 else 50)

if __name__ == '__main__':
    sensor = CO2Sensor('co2_sensor_001')
    print(f'CO₂ Reading: {sensor.read_value():.2f} ppm')
