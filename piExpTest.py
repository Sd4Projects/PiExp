#!/home/pi/venv/bin/python

# This program released under OHL Version 1.2
#
# Software install notes
#
# sudo apt install python3-full       do BEFORE venv install
# python3 -m venv ./venv
# sudo ./venv/bin/pip3 install adafruit-blinka
# sudo ./venv/bin/pip3 install adafruit-circuitpython-ads1x15
# sudo ./venv/bin/pip3 install sparkfun-qwiic-oled-display
# sudo ./venv/bin/pip3 install adafruit-circuitpython-ssd1306
# sudo ./venv/bin/pip3 install adafruit-circuitpython-24lc32
#
# sudo vi /home/pi/venv/lib/python3.11/site-packages/adafruit_24lc32.py
#    change _MAX_SIZE_I2C = const(0x1000) to  _MAX_SIZE_I2C = const(0x8000)
#
# for pi hostname w2.local
#    scp font5x8.bin pi@w2.local:/home/pi  <-- for ssd1306, missing font from GitHub
  
import RPi.GPIO as GPIO
import sys
import time
import datetime
import math
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import adafruit_24lc32
import adafruit_ssd1306

SWPIN = 5
LEDOUT = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(SWPIN, GPIO.IN)
GPIO.setup(LEDOUT, GPIO.OUT)

# NTC sensor , using Adafruit #P372 NTC 10K Thermistor
R1 = 10000
Vcc=3.31
Bc = 3950
Tnom = 25
Rntc = 10000
temperatureF = 32.0

def do_quit():
    GPIO.cleanup()
    sys.exit(0)

def read_Temp():
    global temperatureF

    adsChan2 = AnalogIn(ads, ADS.P2)
    Vr2 = adsChan2.voltage
    R2=Vr2*R1/(Vcc-Vr2)
    steinhart = R2 / Rntc
    steinhart = math.log(steinhart)
    steinhart /= Bc
    steinhart += 1 / (Tnom + 273.15)
    steinhart = 1 / steinhart
    steinhart -= 273.15
    temperatureF = (steinhart * 9.0 / 5.0) + 32.0

i2c = board.I2C()
ads = ADS.ADS1115(i2c)

oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3d)
oled.show()

GPIO.output(LEDOUT, True);

eepromSize = 0
try:
    eeprom = adafruit_24lc32.EEPROM_I2C(i2c)
    print("Found 24lc32 EEPROM at 0x50")
    eepromSize = len(eeprom)
    print("Eeprom Size: {}".format(len(eeprom)))
    eeprom[1] = 2        # test read write to eeprom
    print(eeprom[1])
    eeprom[1] = 4
    print(eeprom[1])
    print("")
except:
    print("24lc32 EEPROM Hardware or Code Error")


while True:
    if GPIO.input(SWPIN) == 1:      # high(pulled up) = switch off
        read_Temp()
        oled.fill(0)
        curTime = "Time: " + datetime.datetime.now().strftime("%H:%M:%S")
        oled.text(curTime, 30, 10 ,1)         # H V
        curTemp = "TempF: {0:.3f}".format(temperatureF)
        oled.text(curTemp, 30, 30 ,1)
        oled.text("Eeprom: " + str(eepromSize), 30, 50 ,1)
        oled.show()
    else:
        print("Run done")
        GPIO.output(LEDOUT, False);
        do_quit()
    time.sleep(0.2)

