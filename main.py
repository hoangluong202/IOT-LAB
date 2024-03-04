from adafruit_mqtt import Adafruit_MQTT
import time
import random

adafruit_mqtt = Adafruit_MQTT()

while True:
    time.sleep(10)
    temp = random.randint(0, 50)
    hum = random.randint(0, 100)
    light = random.randint(0, 100)
    print('Cap nhat cam bien nhiet do: {0}.'.format(temp))
    adafruit_mqtt.client.publish(adafruit_mqtt.AIO_FEED_ID_SENSOR_1, temp)
    print('Cap nhat cam bien do am: {0}.'.format(hum))
    adafruit_mqtt.client.publish(adafruit_mqtt.AIO_FEED_ID_SENSOR_2, hum)
    print('Cap nhat cam bien anh sang: {0}.'.format(light))
    adafruit_mqtt.client.publish(adafruit_mqtt.AIO_FEED_ID_SENSOR_3, light)
    
