import apgiotboard
import time
from machine import ADC



BTN1  = 1
BTN2  = 2
LONG_ms = 2000
LED_count = 6 

# interne temp sensor verbonden aan pin 4 ADC
temp_sensor = ADC(4)

def exit_pressed():
    #  nakijken als beide knoppen ingedrukt zijn long_ms
    start = time.ticks_ms()
    while apgiotboard.button_pressed(BTN1) and apgiotboard.button_pressed(BTN2):
        if time.ticks_diff(time.ticks_ms(),start) >=LONG_ms:
            return True
        time.sleep_ms(10)
    return(False)


def rd_intern_temp():
    adc_value = temp_sensor.read_u16()

    # ADC omzetten naar voltage 
    volt = adc_value*(3.3 / 65535.0)

    # temp omrekenen op bassis van sensor
    temp_celsius = 27 - (volt - 0.706) / 0.001721

    return temp_celsius
tempC = rd_intern_temp()
print("internal Tempratuur", tempC, "°C")
