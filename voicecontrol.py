import random
import sys
import time
import RPi.GPIO as GPIO
from Adafruit_IO import MQTTClient
KEY      = '9553c8b1d1264fb290aa088748c74c07'    
USERNAME = 'smarthome24x7'  
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(2,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(14,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)

 
def connected(client):
   
    print ('Connected to Server Listening for changes...')
    client.subscribe('TV')
    client.subscribe('AC')
    client.subscribe('Fan')
    client.subscribe('Light')
    client.subscribe('Pump')
    client.subscribe('Refrigerator')
    client.subscribe('Water Heater')
 
def disconnected(client):
    print ('Disconnected from Adafruit IO!')
    sys.exit(1)
 
def message(client, feed_id, status):
            
    if feed_id == 'AC':
        if status=='ON':
            print("AC ON")
            GPIO.output(14,GPIO.HIGH)
        else:
            print("AC OFF")
            GPIO.output(14,GPIO.LOW)
            
    elif feed_id == 'Fan':
        if status=='ON':
            print("Fan ON")
            GPIO.output(3,GPIO.HIGH)
        else:
            print("Fan OFF")
            GPIO.output(3,GPIO.LOW)
            
    elif feed_id == 'TV':
        if status=='ON':
            print("TV ON")
            GPIO.output(4,GPIO.HIGH)

        else:
            print("TV OFF")
            GPIO.output(4,GPIO.LOW)
            
            
    elif feed_id == 'Light':
        if status=='ON':
            print("Light ON")
            GPIO.output(2,GPIO.HIGH)
        else:
            print("Light OFF")
            GPIO.output(2,GPIO.LOW)
            
    elif feed_id == 'Pump':
        if status=='ON':
            print("Pump ON")
            GPIO.output(15,GPIO.HIGH)
        else:
            print("Pump OFF")
            GPIO.output(15,GPIO.LOW)
            
    elif feed_id == 'Refrigerator':
        if status=='ON':
            print("Refrigerator ON")
            GPIO.output(17,GPIO.HIGH)
        else:
            print("Refrigerator OFF")
            GPIO.output(17,GPIO.LOW)
    
            
    elif feed_id == 'Water Heater':
        if status=='ON':
            print("Water Heater ON")
            GPIO.output(18,GPIO.HIGH)
        else:
            print("Water Heater OFF")
            GPIO.output(18,GPIO.LOW)

            
        
client = MQTTClient(USERNAME,KEY) 
client.on_connect    = connected
client.on_disconnect = disconnected
client.on_message    = message
client.connect() 
client.loop_blocking()
GPIO.cleanup()
