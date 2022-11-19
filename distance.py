from machine import Pin
import utime

# Ground To Ground
# ECHO to I2C1 SDA (GP0, Physical pin 4)
# TRIG to I2C1 SCL (GP1, Physical pin 5)
# VCC to 3V3(OUT) (Physical Pin 36)

trigger = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)
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
   distance = (timepassed * 0.0343) / 2
   print("The distance from object is ",distance,"cm")
while True:
   ultra()
   utime.sleep(1)
