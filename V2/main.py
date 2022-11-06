from my_lcd import lcd_print
from UltraSonic import ultra
from LED_Distance import led_distance
import time

while True:
    dist_s, dist = ultra()
    led_distance(dist)
    lcd_print(dist_s)
    time.sleep(0.5)
