import RPi.GPIO as GPIO
import time
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

ltransmit=23
#lreceiver=24
Repin=24
buzzer=25
GPIO.setup(ltransmit,GPIO.OUT)
GPIO.output(ltransmit,GPIO.LOW)
time.sleep(2)
GPIO.setup(buzzer,GPIO.OUT)
time.sleep(2)
GPIO.output(buzzer,GPIO.LOW)
#def Rec(Repin):
GPIO.setup(Repin,GPIO.IN)
	
	
#try:
while True:
	GPIO.output(ltransmit,GPIO.HIGH)
	 
	time.sleep(0.1)
	#GPIO.output(ltransmit,GPIO.LOW)
	if GPIO.input(Repin):
		print"safe"
		GPIO.output(buzzer,GPIO.LOW)
		time.sleep(2)
	else:
		print"not safe "
		GPIO.output(buzzer,GPIO.HIGH)
		time.sleep(2)
except KeyboardInterrupt:
#time.sleep(20)
GPIO.output(ltransmit,GPIO.LOW)
GPIO.output(buzzer,GPIO.LOW)		
GPIO.cleanup()



