from machine import Pin
from utime import sleep

# Ground To Ground
# Out to GP28 (Physical Pin 34)
# VCC to VBUS (Physical Pin 40)
pir_sensor = Pin(28, Pin.IN)

# Ground To Ground
# In to GP15 (Physical Pin 20)
# VCC to 3V3(OUT) (Physical Pin 36)
relay = Pin(15, Pin.OUT)

# Short Leg To One End Of Resistor And Other End Of Resistor To Ground
# Long Leg to GP9 (Physical Pin 12)
led = Pin(9, Pin.OUT)

# Short Leg To Ground
# Long Leg to GP16 (Physical Pin 21)
buzzer = Pin(16, Pin.OUT)

while 1:
    if pir_sensor.value() == 1:
        relay.off()
        sleep(3)
    else:
        relay.on()
            
relay.on()
print("Exiting")

