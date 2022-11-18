from machine import Pin
from utime import sleep

# Ground To Ground
# Out to GP28 (Physical Pin 34)
# VCC to VBUS (Physical Pin 40)
pir_sensor = Pin(28, Pin.IN, Pin.PULL_UP)

# Short Leg To Ground
# Long Leg to GP16 (Physical Pin 21)
buzzer = Pin(16, Pin.OUT)

# Short Leg To One End Of Resistor And Other End Of Resistor To Ground
# Long Leg to GP9 (Physical Pin 12)
led = Pin(9, Pin.OUT)

try:
    while True:
        if pir_sensor.value() == 1:
            for i in range(5):
                buzzer.toggle()
                led.toggle();
                sleep(0.1)
        else:
            buzzer.off();
            led.off();

except KeyboardInterrupt:
    buzzer.off()
    print("Exiting")





