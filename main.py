import sys
import time
import random
from Adafruit_IO import MQTTClient

#Variables
ADAFRUIT_IO_USERNAME = "hl01012002"
ADAFRUIT_IO_KEY = "aio_anJs84KwvObUuJYkl1abRQfVKU5h"
AIO_FEED_ID_BUTTON_1 = "button1"
AIO_FEED_ID_BUTTON_2 = "button2"
AIO_FEED_ID_SENSOR_1 = "sensor1"
AIO_FEED_ID_SENSOR_2 = "sensor2"
AIO_FEED_ID_SENSOR_3 = "sensor3"

#Functions
def connected(client):
  print('Connected to Adafruit IO!')
  client.subscribe(AIO_FEED_ID_BUTTON_1)
  client.subscribe(AIO_FEED_ID_BUTTON_2)

def subcribe(client, userdata, mid, granted_qos):
  print('Subscribed to {0} with QoS {1}'.format(mid, granted_qos[0]))

def disconnected(client):
  print('Disconnected from Adafruit IO!')
  sys.exit(1)

def message(client, feed_id, payload):
  print('Feed {0} received new value: {1}'.format(feed_id, payload))


client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subcribe
client.connect()
client.loop_background()

while True:
    temp = random.randint(0, 50)
    hum = random.randint(0, 100)
    light = random.randint(0, 100)
    print('Publishing {0} to {1}.'.format(temp, AIO_FEED_ID_SENSOR_1))
    client.publish(AIO_FEED_ID_SENSOR_1, temp)
    print('Publishing {0} to {1}.'.format(hum, AIO_FEED_ID_SENSOR_2))
    client.publish(AIO_FEED_ID_SENSOR_2, hum)
    print('Publishing {0} to {1}.'.format(light, AIO_FEED_ID_SENSOR_3))
    client.publish(AIO_FEED_ID_SENSOR_3, light)
    time.sleep(10)
