import machine
from time import sleep

led = machine.Pin("LED", machine.Pin.OUT)


def blink():
    led.off()
    print("Off")
    sleep(1)
    led.on()
    print("On")
    sleep(1)
