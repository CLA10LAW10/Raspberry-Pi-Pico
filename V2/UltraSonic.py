from machine import Pin
import utime

# Identify input to output pins of the PICO.
# Ultrasonic Pins
trigger = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)


# Ultrasonic Function
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
    print("The distance from object is ", dist, "cm")
    dist_s = str(dist)
    return dist_s, dist
