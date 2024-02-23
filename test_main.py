## import class Adafruit_MQTT
from main_oop import Adafruit_MQTT

def your_callback_function(client, userdata, message):
    print("Received: " + message.payload)

adafruit_mqtt = Adafruit_MQTT()
adafruit_mqtt.setReceiveCallback(your_callback_function)


while True:
    pass