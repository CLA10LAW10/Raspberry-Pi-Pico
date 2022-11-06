import utime

from machine import I2C
from machine import Pin
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

I2C_ADDR     = 0x27
I2C_NUM_ROWS = 4
I2C_NUM_COLS = 20

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

#my custom display commands
#clear screen
def lcd_print(dist_s):
    lcd.clear()
    lcd.move_to(0,0)
    lcd.putstr("Distance = ")
    lcd.move_to(3,1)
    lcd.putstr(dist_s + " cm")
    utime.sleep(1)
    lcd.clear()