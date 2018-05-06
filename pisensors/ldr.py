import RPi.GPIO as GPIO
import time
from time import sleep
DEBUG = 1
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
motor1=23
motor2=24
GPIO.setup(motor1,GPIO.OUT)
GPIO.setup(motor2,GPIO.OUT)

def RCtime (RCpin):
	reading = 0
	GPIO.setup(RCpin,GPIO.OUT)
	GPIO.output(RCpin,GPIO.LOW)
	time.sleep(0.00001)
	
	GPIO.setup(RCpin,GPIO.IN)
	
	while (GPIO.input(RCpin)==GPIO.LOW):
		reading +=1
	return reading
def forward():
	GPIO.output(motor1,GPIO.HIGH)
def back():
	GPIO.output(motor2,GPIO.HIGH)
try:
	while True:
		print RCtime(18)
		time.sleep(1)
		if RCtime(18)>=100:
			forward()
		else:
			back()
		time.sleep(0.0001)

except KeyboardInterrupt:
	GPIO.cleanup()

