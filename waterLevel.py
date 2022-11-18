from machine import Pin
from utime import sleep

try:
    while 1:
        pin = Pin(7)
        print(pin.value())

        if pin.value() == 1:
            buzzer = Pin(16,Pin.OUT)
            buzzer.on()
            sleep(0.1)
            buzzer.off()
            sleep(0.1)

except KeyboardInterrupt:
    buzzer.off()
    print("Exiting")


