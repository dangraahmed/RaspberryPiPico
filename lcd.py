from machine import I2C, Pin
from time import sleep
from pico_i2c_lcd import I2cLcd

# Ground To Ground
# VCC to VBUS (Physical Pin 40)
# SDA to I2C0 SDA (GP0, Physical pin 1)
# SCL to I2C0 SCL (GP1, Physical pin 2)
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=200000)

I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

try:
    while True:
        print(I2C_ADDR)
        lcd.blink_cursor_on()
        lcd.putstr("I2C Address:"+str(I2C_ADDR)+"\n")
        lcd.putstr("Tom's Hardware")
        sleep(2)
        lcd.clear()
        lcd.putstr("I2C Address:"+str(hex(I2C_ADDR))+"\n")
        lcd.putstr("Haajra Dangra")
        sleep(2)
        lcd.blink_cursor_off()
        lcd.clear()
        lcd.putstr("Backlight Test")
        for i in range(10):
            lcd.backlight_on()
            sleep(0.2)
            lcd.backlight_off()
            sleep(0.2)
        lcd.backlight_on()
        lcd.hide_cursor()
        for i in range(20):
            lcd.putstr(str(i))
            sleep(0.4)
            lcd.clear()
except KeyboardInterrupt:
    lcd.clear()
    lcd.backlight_off()


