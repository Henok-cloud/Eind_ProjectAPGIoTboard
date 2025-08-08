import apgiotboard
import time
from machine import ADC



BTN1  = 1
BTN2  = 2
LED_GREEN = 1
LED_RED = 2 
LED_START = 3 
LONG_ms = 2000
LED_COUNT = 6 

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
        
        # lees en afronden
        t_int =rd_intern_temp()
        if t_int < 0:
            t_int = 0

        #bepalen of in beriek (0-63 celsius) blijven
        if t_int <=(1 << LED_COUNT) - 1:
            # binnen bereiek  groen aan, rood uit
            apgiotboard.led(LED_GREEN).on()
            apgiotboard.led(LED_RED).off()
            val = t_int
        
        else:
            # te hoog temp rood aan, groen uit
            apgiotboard.led(LED_GREEN).off()
            apgiotboard.led(LED_RED).on()
            val = (1 << LED_COUNT) -1 
        
        # Toon op leds 3-8
        for i in range(LED_COUNT):
            bit = (val >> i) & 1
            led = apgiotboard.led(LED_START + i)
            if bit:
                led.on()
            else:
                led.off()


        # debug 
        bits_str = ''.join('1'if (val >>(LED_COUNT-1-j)) & 1 else '0' for j in range(LED_COUNT))
        print(f"Temp:{t_int} °C→ {bits_str}")

        time.sleep(1)