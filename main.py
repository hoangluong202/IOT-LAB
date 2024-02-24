import sys
import time
import random
from Adafruit_IO import MQTTClient
from simple_ai import image_detector

#Variables
ADAFRUIT_IO_USERNAME = "hl01012002"
ADAFRUIT_IO_KEY = "aio_eEfB69BuOU6Pq4UGIbqeaGWGenIf"
AIO_FEED_ID_BUTTON_1 = "button1"
AIO_FEED_ID_BUTTON_2 = "button2"
AIO_FEED_ID_SENSOR_1 = "sensor1"
AIO_FEED_ID_SENSOR_2 = "sensor2"
AIO_FEED_ID_SENSOR_3 = "sensor3"
AI0_FEED_ID_AI = "ai"

#Functions
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


client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()

ai_counter = 3
global pre_result
pre_result = ""
while True:
    ai_counter -= 1
    if ai_counter == 0:
        ai_counter = 3
        result = image_detector()
        print("AI Output:", result)
        if(result != pre_result):
            client.publish(AI0_FEED_ID_AI, result)
            pre_result = result
    time.sleep(1)
