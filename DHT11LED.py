import Adafruit_DHT
import time
import sys
import RPi.GPIO as GPIO
import os
from time import sleep
import urllib.request
 
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4
myAPI = "PUTYOURAPIKEYHERE"
myDelay = 5
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.output(17,GPIO.HIGH)


print ('starting...')
baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI
print (baseURL)
 
while True:
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        print("Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity))
        
        f = urllib.request.urlopen(baseURL+"&field1=%s&field2=%s"%(temperature, humidity))
        print (f.read())
        print ("tempC " + str(temperature) + ", humidity " + str(humidity))
        f.close()
        
        if (temperature > 27 or humidity > 70):
            print("Uma das condicoes foi satisfeita, acionar LED")
            GPIO.output(17,GPIO.LOW)
        
            
    else:
        print("Sensor failure. Check wiring. Desligando LED");
        GPIO.output(17,GPIO.HIGH)
    time.sleep(myDelay);
