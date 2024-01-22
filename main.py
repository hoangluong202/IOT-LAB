import sys
import time
import random
import serial.tools.list_ports
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
  if isMicrobitConnected:
        ser.write((str(payload) + "#").encode())


client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subcribe
client.connect()
client.loop_background()

def getPort():
    ports = serial.tools.list_ports.comports()
    N = len(ports)
    commPort = "None"
    for i in range(0, N):
        port = ports[i]
        strPort = str(port)
        if "USB Serial Device" in strPort:
            splitPort = strPort.split(" ")
            commPort = (splitPort[0])
    return commPort

isMicrobitConnected = False
if getPort() != "None":
    ser = serial.Serial( port=getPort(), baudrate=115200)
    isMicrobitConnected = True


def processData(data):
    data = data.replace("!", "")
    data = data.replace("#", "")
    splitData = data.split(":")
    print(splitData)
    if splitData[1] == "TEMP":
        client.publish(AIO_FEED_ID_SENSOR_1, splitData[2])

mess = ""
def readSerial():
    bytesToRead = ser.inWaiting()
    if (bytesToRead > 0):
        global mess
        mess = mess + ser.read(bytesToRead).decode("UTF-8")
        while ("#" in mess) and ("!" in mess):
            start = mess.find("!")
            end = mess.find("#")
            processData(mess[start:end + 1])
            if (end == len(mess)):
                mess = ""
            else:
                mess = mess[end+1:]

while True:
    if isMicrobitConnected:
        readSerial()
    time.sleep(1)

