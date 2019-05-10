import random
import sys
import time
import RPi.GPIO as GPIO
import bluetooth 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(2,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(14,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)

while True:
    try:        
        server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM ) 
        port = 1
        server_sock.bind(("",port)) 
        server_sock.listen(1) 
        client_sock,address = server_sock.accept() 
        print "Accepted connection from ",address 
        while True: 
            recvdata = client_sock.recv(1024) 
            #print "Received \"%s\" through Bluetooth" % recvdata 
                
            if recvdata == 'AcON':
                print("AC ON")
                GPIO.output(2,GPIO.HIGH)        
            elif recvdata == 'AcOFF':
                print("AC OFF")
                GPIO.output(2,GPIO.LOW)
                
            elif recvdata == 'FanON':
                print("Fan ON")
                GPIO.output(3,GPIO.HIGH)
            elif recvdata == 'FanOFF':
                print("FanOFF")
                GPIO.output(3,GPIO.LOW)
                
            elif recvdata == 'TvON':
                print("TvON")
                GPIO.output(4,GPIO.HIGH)
            elif recvdata == 'TvOFF':
                print("TvOFF")
                GPIO.output(4,GPIO.LOW)
                
                
            elif recvdata == 'RefrigeratorON':
                print("RefrigeratorON")
                GPIO.output(14,GPIO.HIGH)
            elif recvdata == 'RefrigeratorOFF':
                print("RefrigeratorOFF")
                GPIO.output(14,GPIO.LOW)
                
                
            elif recvdata == 'PumpON':
                print("PumpON")
                GPIO.output(15,GPIO.HIGH)            
            elif recvdata == 'PumpOFF':
                print("PumpOFF")
                GPIO.output(15,GPIO.LOW)
                
                
            elif recvdata == 'HeaterON':
                print("HeaterON")
                GPIO.output(17,GPIO.HIGH)
            elif recvdata == 'HeaterOFF':
                print("HeaterOFF")
                GPIO.output(17,GPIO.LOW)
                
            elif recvdata == 'LightON':
                print("LightON")
                GPIO.output(18,GPIO.HIGH)
            elif recvdata == 'LightOFF':
                print("LightOFF")
                GPIO.output(18,GPIO.LOW)
                     
        client_sock.close() 
        server_sock.close()
        GPIO.cleanup()
    except:
        print("DisConnected")
