import paho.mqtt.client as mqtt, json, time
from backend.db import save_reading

def on_connect(client, userdata, flags, rc):
    client.subscribe('sensors/#')

def on_message(client, userdata, msg):
    try:
        data = json.loads(msg.payload)
        save_reading(data['id'], data['type'], data['value'])
    except Exception as e:
        print(f'[ERROR] {e}')

def on_disconnect(client, userdata, rc):
    while True:
        try:
            client.reconnect()
            break
        except:
            time.sleep(5)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect
client.connect('mqtt', 1883)
client.loop_forever()
