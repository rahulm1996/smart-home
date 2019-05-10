import os
import time
import RPi.GPIO as GPIO
import smtplib
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(13,GPIO.IN)
GPIO.setup(6, GPIO.IN)  
def sendemail(subject,msg):
	try:
		server=smtplib.SMTP('smtp.gmail.com:587')
		server.ehlo()
		server.starttls()
		server.login('my.smarthome24x7@gmail.com','Smart@321')
		message='Subject:{}\n\n{}'.format(subject,msg)
		server.sendmail('my.smarthome24x7@gmail.com','rockrahul180@gmail.com',message)
		server.quit()
		if(subject=="Weather Alert From Home"):
			print('mail sent for weather alert')
		elif(subject=="Security Alert From Home"):
			print('mail sent for security alert')
	except:
		print('unscussfull')
print ("alert program started")
while True:
	time.sleep(10)
	print ("in mailing loop")
	if(GPIO.input(13)==0):
		print("RAIN")
		msg="Is Raining at home if there is any londry dring then take it in."
		sendemail("Weather Alert From Home",msg)	
		


	if(GPIO.input(6)==1):
		print("Intrusion")
		msg="There is an suspicious movement near your home while you were not away"
		sendemail("Security Alert From Home",msg)
