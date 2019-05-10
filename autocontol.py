import time
import RPi.GPIO as GPIO
import sys
import Adafruit_DHT
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(26,GPIO.IN)
GPIO.setup(2,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
TRIG = 0 
ECHO = 5
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
def temp():
    humidity, temperature = Adafruit_DHT.read_retry(11, 19)#pin no. 19
    return temperature
def distnce():
    GPIO.output(TRIG, False)
    print "Waiting For Sensor To Settle"
    time.sleep(2)

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO)==0:
        pulse_start = time.time()

    while GPIO.input(ECHO)==1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150

    distance = round(distance, 2)
    print(distance)
    return distance
    
while True:
    print("auto conrol loop")
    time.sleep(1)
    if(GPIO.input(26)==1):
        print("Light ON")
        GPIO.output(2,True)
    elif(GPIO.input(26)==0):
        print("Light OFF")
        GPIO.output(2,False)
        
    if(temp()>40.0):
        print("Fan ON")
        GPIO.output(3,True)
    elif(temp()<=40.0):
        print("Fan OFF")
        GPIO.output(3,False)
        
    if(distnce() <= 10.0):
        
        print("Door Open",distnce())
        GPIO.output(27,True)
    elif(distnce() >10.0):
        print("Door Colosed",distnce())
        GPIO.output(27,False)
  
  

