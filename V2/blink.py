import machine
from time import sleep

led = machine.Pin("LED", machine.Pin.OUT)


def blink():
    led.off()
    sleep(1)
    led.on()
    sleep(1)


while True:
    blink()
