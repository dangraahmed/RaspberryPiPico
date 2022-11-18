from machine import Pin
from utime import sleep

try:
    while 1:
        buzzer = Pin(16,Pin.OUT)
        led = Pin(15,Pin.OUT)
        buzzer.on()
        led.on()
        sleep(0.1)
        buzzer.off()
        led.off()
        sleep(0.1)

except KeyboardInterrupt:
    buzzer.off()
    print("Exiting")


