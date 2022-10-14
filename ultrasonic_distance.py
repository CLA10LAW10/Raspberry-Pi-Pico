import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BCM)

TRIG = 2
ECHO = 3
RED = 4
YELLOW = 17
GREEN = 27
BLUE = 22

GPIO.setup(RED,GPIO.OUT)
GPIO.setup(YELLOW,GPIO.OUT)
GPIO.setup(GREEN,GPIO.OUT)
GPIO.setup(BLUE,GPIO.OUT)

print ("Distance Measurement In Progress")
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.output(TRIG, False)

print ("Waiting For Sensor To Settle")

time.sleep(2)
def distance():
  GPIO.output(TRIG, True)

  time.sleep(0.00001)

  GPIO.output(TRIG, False)

  while GPIO.input(ECHO)==0:
    pulse_start = time.time()
  while GPIO.input(ECHO)==1:
    pulse_end = time.time()
  pulse_duration = pulse_end - pulse_start
  distance = pulse_duration * 17150
  distance = round(distance, 2)
  return distance
try:
  while True:
    dist = distance()
    print ("Distance:",dist,"cm")
    if (dist <= 91):
      GPIO.output(RED,GPIO.HIGH)
      GPIO.output(YELLOW,GPIO.LOW)
      GPIO.output(GREEN,GPIO.LOW)
      GPIO.output(BLUE,GPIO.LOW)
      time.sleep(1)
    elif (dist >  91 and dist <= 305):
      GPIO.output(YELLOW,GPIO.HIGH)
      GPIO.output(RED,GPIO.LOW)
      GPIO.output(GREEN,GPIO.LOW)
      GPIO.output(BLUE,GPIO.LOW)
      time.sleep(1)
    elif (dist >  305 and dist <= 500):
      GPIO.output(GREEN,GPIO.HIGH)
      GPIO.output(RED,GPIO.LOW)
      GPIO.output(YELLOW,GPIO.LOW)
      GPIO.output(BLUE,GPIO.LOW)
      time.sleep(1)
    else:
      GPIO.output(BLUE,GPIO.HIGH)
      GPIO.output(RED,GPIO.LOW)
      GPIO.output(YELLOW,GPIO.LOW)
      GPIO.output(GREEN,GPIO.LOW)
      time.sleep(1)
# Reset by pressing CTRL + C
except KeyboardInterrupt:
    print("Measurement stopped by User")
    GPIO.cleanup()