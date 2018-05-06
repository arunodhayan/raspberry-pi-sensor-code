import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)
print"motor Forward"
GPIO.output(18,GPIO.HIGH)
time.sleep(10)
print"motor off"

GPIO.output(18,GPIO.LOW)
time.sleep(4)
print "motor Reverse"
GPIO.output(25,GPIO.HIGH)
time.sleep(5)
print"motor off"
GPIO.output(25,GPIO.LOW)
