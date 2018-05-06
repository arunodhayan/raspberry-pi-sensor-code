#!/usr/bin/python
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)


def trigger():
    GPIO.output(18,False)
try:
    trigger()

except KeyboardInterrupt:
    print ("Quit")
    GPIO.cleanup()

