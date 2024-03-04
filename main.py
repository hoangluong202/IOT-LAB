import sys
import time
import random
import os
from Adafruit_IO import MQTTClient
from dotenv import load_dotenv
from simple_ai import image_detector

load_dotenv()  # take environment variables from .env.

#Variables
ADAFRUIT_IO_USERNAME = os.getenv("ADAFRUIT_IO_USERNAME")
ADAFRUIT_IO_KEY = os.getenv("ADAFRUIT_IO_KEY")
AIO_FEED_ID_BUTTON_1 = "button1"
AIO_FEED_ID_BUTTON_2 = "button2"
AIO_FEED_ID_SENSOR_1 = "sensor1"
AIO_FEED_ID_SENSOR_2 = "sensor2"
AIO_FEED_ID_SENSOR_3 = "sensor3"
AI0_FEED_ID_AI = "ai"

def connected(client):
  print("Ket noi thanh cong...")
  client.subscribe(AIO_FEED_ID_BUTTON_1)
  client.subscribe(AIO_FEED_ID_BUTTON_2)

def subscribe(client, userdata, mid, granted_qos):
  print("Subscribe thanh cong...")

def disconnected(client):
  print("Ngat ket noi...")
  sys.exit(1)

def message(client, feed_id, payload):
  print("Nhan du lieu: " + payload)

client = MQTTClient(ADAFRUIT_IO_USERNAME , ADAFRUIT_IO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.on_subscribe = subscribe
client.connect()
client.loop_background()

while not client.is_connected():
    print('Waiting for connection...')
    time.sleep(1)

while True:
  pass