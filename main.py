from uart import *
from adafruit_mqtt import Adafruit_MQTT
import time

adafruit_mqtt = Adafruit_MQTT()
time.sleep(5)
while True:
    readSerial(adafruit_mqtt.client)
    time.sleep(1)