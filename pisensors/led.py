import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
print"led on"
GPIO.setup(18,GPIO.OUT)
time.sleep(1)
GPIO.output(18,GPIO.HIGH)
time.sleep(10)
print"led off"
GPIO.output(18,GPIO.LOW)

