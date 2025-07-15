import time
import apgiotboard
import math
from machine import PWM 

BTN1 = 1
BTN2 = 2
LONG_MS = 2000
LED_START = 3
LED_COUNT = 6

_scroll_idx = LED_START
_fade_idx   = LED_START


def run():
    """
    LED-show met vier effecten:
      1) links afrollen  (rol over LEDs van links naar rechts)
      2) rechts afrollen (rol over LEDs van rechts naar links)
      3) fade-in chase    (chase met oplopende intensiteit)
      4) regenval-effect (random leds vallen als regendruppels)
    - Speed wordt geregeld door de potmeter.
    - BTN1 = volgende effect, BTN2 = vorig effect.
    - Lange gezamenlijke druk (≥ LONG_MS) = exit naar main.
    """
    effect = 0
    prev1 = prev2 = False
    t1 = t2 = 0
    t_both = 0
    last_step = time.ticks_ms()
    apgiotboard.all_leds_off()



    while True:
        now = time.ticks_ms()
        b1 = apgiotboard.button_pressed(BTN1)
        b2 = apgiotboard.button_pressed(BTN2)

        # Exit : lang gezamelijke druk 
        if b1 and b2:
            if t_both == 0:
                t_both = now
            elif time.ticks_diff(now, t_both) >= LONG_MS:
                apgiotboard.all_leds_off()
                return
        else:
            t_both = 0
        
        # Effect wisselen met BTN1(next)
        if b1 and not prev1:
            effect = (effect + 1)%4
            apgiotboard.all_leds_off()
            last_step = now
        prev1 = b1

        # effect wisselen met BTN2 (vorige)
        if b2 and not prev2:
            effect =(effect - 1) % 4
            apgiotboard.all_leds_off()
            last_step = now
        prev2 = b2

        # delay aflezen van pot
        delay = _get_delay()

        # Show uitvoeren
        if time.ticks_diff(now, last_step) >= delay:
            if effect == 0:
                _scroll(left_to_right=True)
            elif effect == 1:
                _scroll(left_to_right =False)
            elif effect == 2:
                _fade_chase()
            else:
                _rain()
            last_step = now
        time.sleep_ms(10)

def _get_delay():
    v = apgiotboard.dial_value()
    return int((300-50)*(65535 - v)/65535 + 50)

def _scroll(left_to_right = True):

    global _scroll_idx
    apgiotboard.all_leds_off()
    apgiotboard.led(_scroll_idx).on()
    if left_to_right:
        _scroll_idx += 1
        if _scroll_idx >= LED_START + LED_COUNT:
            _scroll_idx = LED_START
    else:
        _scroll_idx -= 1
        if _scroll_idx < LED_START:
            _scroll_idx = LED_START + LED_COUNT - 1

def _fade_chase():


def _rain():

    import urandom
    apgiotboard.all_leds_off()
    i = urandom.getrandbits(3)% LED_COUNT
    apgiotboard.led(LED_START + i).on()