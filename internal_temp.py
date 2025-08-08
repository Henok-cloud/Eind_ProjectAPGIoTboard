import apgiotboard
import time
from machine import ADC



BTN1  = 1
BTN2  = 2
LED_START = 3 
LONG_ms = 2000
LED_OFFSET = 3 

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

    return int(round(temp_celsius))
tempC = rd_intern_temp()
print("internal Tempratuur", tempC, "°C")

def run():
    apgiotboard.all_leds_off()
    while True:
        # exit bij lang gezamelijk drukken
        if exit_pressed():
            apgiotboard.all_leds_off()
            return
        
        # meet temp en zet om naar 6 bit tow's complement
        t_int = rd_intern_temp()
        val = t_int & 0x3f

        #toon op leds(6)
        for i in range(6):
            if (val >> i) & 1:
                apgiotboard.led(LED_OFFSET + i).on()
            else:
                apgiotboard.led(LED_OFFSET + i).off()


        # debug 
        bits_str = ''.join('1'if (val >>(5 -j)) & 1 else '0' for j in range(6))
        print(f"Temp:{t_int} °C→ {bits_str}")

        time.sleep(1)