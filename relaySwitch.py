from machine import Pin
from utime import sleep

# Ground To Ground
# In to GP15 (Physical Pin 20)
# VCC to 3V3(OUT) (Physical Pin 36)
relay = Pin(15, Pin.OUT)
relay.off()
while 1:
    print(machine.RTC())
    relay.on()
    sleep(1)
    relay.off()
    sleep(1)
