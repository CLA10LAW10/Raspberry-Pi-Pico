from machine import Pin

# Identify input to output pins of the PICO.
# LED Pins
RED = Pin(20, Pin.OUT)
YELLOW = Pin(22, Pin.OUT)
GREEN = Pin(17, Pin.OUT)
BLUE = Pin(16, Pin.OUT)


# Light the desired LED indicating the distance from the ultrasonic sensor
def led_distance(dist):

    if dist <= 91:
        RED.high()
        YELLOW.low()
        GREEN.low()
        BLUE.low()
    elif 91 < dist <= 305:
        YELLOW.high()
        RED.low()
        GREEN.low()
        BLUE.low()
    elif 305 < dist <= 500:
        GREEN.high()
        RED.low()
        YELLOW.low()
        BLUE.low()
    else:
        BLUE.high()
        RED.low()
        YELLOW.low()
        GREEN.low()

