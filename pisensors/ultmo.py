import RPi.GPIO as GPIO
import time 
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
Trig=23
Echo=24
Motor=18
Motor1=25
GPIO.setup(Trig,GPIO.OUT)
GPIO.setup(Echo,GPIO.IN)
GPIO.setup(Motor,GPIO.OUT)
GPIO.setup(Motor1,GPIO.OUT)
GPIO.output(Trig,False)
print"distance measurement in progress"
def distance():
	GPIO.output(Trig,True)
	time.sleep(0.000001)
	GPIO.output(Trig,False)
	start = time.time()
	stop = time.time()
	while GPIO.input(Echo)==0:
		start = time.time()
	while GPIO.input(Echo)==1:
                stop = time.time()
	elapsed = stop-start
	distance = (elapsed*34300)/2

	return distance

def forward():
	GPIO.output(Motor,GPIO.HIGH)
def back():
	GPIO.output(Motor1,GPIO.HIGH)
if __name__ =='__main__':
	try:
		while True:
			dist = distance()
			print "distance:%.1f"%dist
		time.sleep(0.005)
		if distance<=100:
			forward()
		else:
			back()

	except KeyboardInterrupt:
		print"measurement stopped by user"
		GPIO.cleanup()




