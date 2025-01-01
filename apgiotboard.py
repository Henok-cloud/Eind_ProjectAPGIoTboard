"""Module for using the AP Graduate IoT board in a more userfriendly way.
Hardware:
GPIO  Hardware
2-9   led1-led8
10    button 2
22    button 1
25    led0 (on raspberry pi)

ADC   Hardware
4     temperature sensor (on raspberry pi)
28    turn knob
"""
import time
from machine import Pin, ADC


MAXLED=8 # constant indicating the highest led number



# h15oef7 + h16oef3
def led(n, use_pin=False):
    """Return the led denoted by n. If use_pin is True, return a Pin object
    for the pin number n instead of a led number. If n is 0 and use_pin is
    not True, return the onboard led."""
    if use_pin:
        return Pin(n, mode=Pin.OUT)
    if n == 0:
        return Pin(25, mode=Pin.OUT)
    if 1 <= n <= MAXLED:
        return Pin(n+1, mode=Pin.OUT)
    raise ValueError(f"Unknown led {n}")


# h15oef10 + h15oef13 (first > last)
def get_leds(first=1, last=MAXLED):
    """Get a list of leds from firstled to lastled inclusive."""
    step = 1 if first <= last else -1
    return [led(id) for id in range(first, last + step, step)]


# h15oef11
def all_leds_off():
    """Turn all leds off (including the onboard green led)."""
    for led in get_leds(first=0):
        led.off()


# h16oef1 + h16oef2 (error handling)
def button(n):
    """Get the button with id."""
    pins = [22, 10]
    if 1 <= n <= len(pins):
        return Pin(pins[n-1], mode=Pin.IN, pull=Pin.PULL_UP)
    raise ValueError(f"Unknown button {n}")


# h16oef4 + h17oef1b
def button_pressed(n, until_released=False):
    """Check if button with id is pressed. Wait until pressed if until_released is set."""
    pressed = button(n).value() == 0
    if not pressed or not until_released:
        return pressed
    while button(n).value() == 0:
        time.sleep_ms(50)
    return True


# h17oef1a
def dial_value(high=65535, invert=True):
    """Get the potmeter value, rescale to [0,high], optional invert."""
    value = int((ADC(Pin(28)).read_u16() * high) / 65535)
    return high - value if invert else value


# The code in the if-statement is only executed when this file is run as script,
# not when imported as a module. It makes it easy to quickly test the functions.
if __name__ == '__main__':
    from time import sleep
    led(2).on()
    sleep(1)
    led(2).off()
