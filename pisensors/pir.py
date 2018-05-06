import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
pir=18
motor=23
motor1=24
GPIO.setup(pir,GPIO.IN)
GPIO.setup(motor,GPIO.OUT)
GPIO.setup(motor1,GPIO.OUT)
time.sleep(2)
print"waiting for sensor to settle"
GPIO.output(motor,GPIO.LOW)
time.sleep(5)
def forward():
	GPIO.output(motor,GPIO.HIGH)
def backward():
	GPIO.output(motor,GPIO.LOW)
while True:
	if GPIO.input(pir):
		print"Motion Detected"
		forward()
		time.sleep(1)
	else:
		backward()
		time.sleep(0.1)
	
	
