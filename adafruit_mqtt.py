import sys
import os
from Adafruit_IO import MQTTClient
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

class Adafruit_MQTT:
    ADAFRUIT_IO_USERNAME = os.getenv("ADAFRUIT_IO_USERNAME")
    ADAFRUIT_IO_KEY = os.getenv("ADAFRUIT_IO_KEY")
    AIO_FEED_ID_BUTTON_1 = "button1"
    AIO_FEED_ID_BUTTON_2 = "button2"
    AIO_FEED_ID_SENSOR_1 = "sensor1"
    AIO_FEED_ID_SENSOR_2 = "sensor2"
    AIO_FEED_ID_SENSOR_3 = "sensor3"

    def __init__(self):
      self.client = MQTTClient(self.ADAFRUIT_IO_USERNAME , self.ADAFRUIT_IO_KEY)
      self.client.on_connect = self.connected
      self.client.on_disconnect = self.disconnected
      self.client.on_message = self.message
      self.client.on_subscribe = self.subscribe
      self.client.connect()
      self.client.loop_background()

    def connected(self,client):
        print("Ket noi thanh cong ...")
        self.client.subscribe(self.AIO_FEED_ID_BUTTON_1)
        self.client.subscribe(self.AIO_FEED_ID_BUTTON_2)

    def subscribe(self,client , userdata , mid , granted_qos):
        print("Subscribe thanh cong ...")

    def disconnected(self,client):
        print("Ngat ket noi ...")
        sys.exit (1)

    def message(self,client , feed_id , payload):
        print("Nhan du lieu tại "+feed_id +': ' + payload)