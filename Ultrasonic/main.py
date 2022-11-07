from machine import Pin
from my_lcd import lcd_print
import utime
import time
from blink import blink


trigger = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)
RED = Pin(20,Pin.OUT)
YELLOW = Pin(22,Pin.OUT)
GREEN = Pin(17,Pin.OUT)
BLUE = Pin(16,Pin.OUT)

def ultra():
   trigger.low()
   utime.sleep_us(2)
   trigger.high()
   utime.sleep_us(5)
   trigger.low()
   while echo.value() == 0:
       signaloff = utime.ticks_us()
   while echo.value() == 1:
       signalon = utime.ticks_us()
   timepassed = signalon - signaloff
   dist = (timepassed * 0.0343) / 2
   print("The distance from object is ",dist,"cm")
   dist_s = str(dist)
   if (dist <= 91):
      RED.high()
      YELLOW.low()
      GREEN.low()
      BLUE.low()
   elif (dist >  91 and dist <= 305):
      YELLOW.high()
      RED.low()
      GREEN.low()
      BLUE.low()
   elif (dist >  305 and dist <= 500):
      GREEN.high()
      RED.low()
      YELLOW.low()
      BLUE.low()
   else:
      BLUE.high()
      RED.low()
      YELLOW.low()
      GREEN.low()
   return dist_s
while True:
   #ultra()
   dist_s = ultra()
   lcd_print(dist_s)
   time.sleep(0.5)
   blink()
   #print ("Distance:",dist,"cm")
    