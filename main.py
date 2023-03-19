from machine import I2C, Pin
from time import sleep
from pico_i2c_lcd import I2cLcd
from mq2 import MQ2
import utime


#Display
# Ground To Ground
# VCC to VBUS (Physical Pin 40)
# SDA to I2C0 SDA (GP0, Physical pin 1)
# SCL to I2C0 SCL (GP1, Physical pin 2)
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=200000)

I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

#Motion Sensor
# Ground To Ground
# Out to GP28 (Physical Pin 34)
# VCC to VBUS (Physical Pin 40)
motion_sensor = Pin(28, Pin.IN, Pin.PULL_UP)

#Distance Sensor
# Ground To Ground
# ECHO to I2C1 SDA (GP2, Physical pin 4)
# TRIG to I2C1 SCL (GP3, Physical pin 5)
# VCC to VBUS (Physical Pin 40)
distance_sensor_echo = Pin(2, Pin.IN)
distance_sensor_trigger = Pin(3, Pin.OUT)

#Gas Sensor
# Ground To Ground
# VCC to VBUS (Physical Pin 40)
# AO to GP26 (Physical Pin 31)
gas_sensor = MQ2(pinData = 26, baseVoltage = 3.3)
gas_sensor.calibrate()

#led
# Short Leg To One End Of Resistor And Other End Of Resistor To Ground
# Long Leg to GP16 (Physical Pin 21)
#buzzer
# Short Leg To Ground
# Long Leg to GP16 (Physical Pin 21)
led_and_buzzer = Pin(16, Pin.OUT)

#relay switch
# Ground To Ground
# In to GP15 (Physical Pin 20)
# VCC to 3V3(OUT) (Physical Pin 36)
relay = Pin(15, Pin.OUT)

rtc=machine.RTC()

def TurnOnTheLight():
    relay.off()

def TurnOffTheLight():
    relay.on()

def ShowMessageOnLCD(messageForLCD):
        lcd.clear()
        lcd.putstr(messageForLCD)

def ClearMessageFromLCD():
        lcd.clear()
        TurnOffTheLight()


def UserAttentionStart(messageForLCD, attentionDuration, sleepTime):
    for i in range(attentionDuration):
        ShowMessageOnLCD(str(i) + ' ' + messageForLCD)
        led_and_buzzer.on()
        sleep(sleepTime)
        led_and_buzzer.off()
        sleep(sleepTime)
        led_and_buzzer.on()
        sleep(sleepTime)
        led_and_buzzer.off()
        sleep(sleepTime)
        led_and_buzzer.on()
        sleep(sleepTime)
        led_and_buzzer.off()
        sleep(sleepTime)

def UserAttentionEnd():
    led_and_buzzer.off();
    ClearMessageFromLCD()

def GetDistance():
    distance_sensor_trigger.low()
    utime.sleep_us(2)
    distance_sensor_trigger.high()
    utime.sleep_us(5)
    distance_sensor_trigger.low()
   
    while distance_sensor_echo.value() == 0:
        signaloff = utime.ticks_us()
    while distance_sensor_echo.value() == 1:
        signalon = utime.ticks_us()
    timepassed = signalon - signaloff
    distance = (timepassed * 0.0343) / 2
    return distance
    
def WriteToLog(messageForLCD):
    file=open("Log.txt","a")
    
    timestamp=rtc.datetime()
    timestring="%04d-%02d-%02d %02d:%02d:%02d"%(timestamp[0:3] + timestamp[4:7])
    file.write(str(timestring) +" : "+ messageForLCD+"\n")
    file.flush()


try:
    ShowMessageOnLCD("Sensors are ready......!")
    sleep(2)
    ClearMessageFromLCD()
    while True:
        utime.sleep(1)
        distance = round(GetDistance())
        lpg = round(gas_sensor.readLPG())
        motion = round(motion_sensor.value())
        
        message = "Distance: " + str(distance) + " LPG: " + str(lpg) + " Motion: " + str(motion)
        print(message)
        ShowMessageOnLCD(message)
        if distance < 5:
            WriteToLog("Distance sensor triggered")
            UserAttentionStart("Distance:" + str(distance), 5, 0.01)
            UserAttentionEnd()
        
        if motion == 1:
            WriteToLog("Motion sensor triggered")
            TurnOnTheLight()
            UserAttentionStart("Motion Sensor", 5, 0.05)
            UserAttentionEnd()
            TurnOffTheLight()

        if lpg > 50:
            WriteToLog("LPG sensor triggered")
            UserAttentionStart("LPG Gas: " + str(lpg), 5, 0.1)
            UserAttentionEnd()

except KeyboardInterrupt:
    UserAttentionEnd()
    print("Exiting")

