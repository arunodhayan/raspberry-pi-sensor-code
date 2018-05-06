from sense_hat import SenseHat
import time
from time import sleep

sense = SenseHat()

blue =(0,0,255)
yellow=(255,255,0)
sense.show_message("RaspberryPi is Awesome",text_colour=yellow)
time.sleep(5)
sense.show_message("Arunodhayan")
#sense.set_pixel(0,2,blue)
#sense.set_pixel(7,4,yellow)
#r = 255
#g = 255
#b = 255

#sense.clear((r,g,b))
