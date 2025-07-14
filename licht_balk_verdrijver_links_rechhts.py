# func1.py
import time
import apgiotboard
from apgiotboard import both_long_pressed


BTN1 = 1
BTN2 = 2
SHORT_MS = 500  #<0,5s Beide knoppen = stop-patroon
LONG_MS = 1000  # >1s beide knoppen = exit
LED_START = 3   # eerste oranje LED
LED_COUNT = 6   # aantal in de balk



def run():
    
    prev1 = False
    prev2 = False
    prev_both = False
    t1      = 0
    t2      = 0
    t_both  = None

    apgiotboard.all_leds_off()

    while True:
        now = time.ticks_ms()
        b1 = apgiotboard.button_pressed(BTN1)
        b2 = apgiotboard.button_pressed(BTN2)
        both = b1 and b2 

        # ---- Beide knoppen event handeling ---
        if both and not prev_both:
            #start gezamelijke druk 
            t_both = now
        elif not both and prev_both and t_both is not None:
            #eind gezameliijke druk 
            dur = time.ticks_diff(now, t_both)
            if dur >= LONG_MS:
                #lang > exit 
                apgiotboard.all_leds_off()
                return
            elif dur < SHORT_MS:
                #kort > STOP-patroon
                _stop_pattern()
            t_both = None
        prev_both = both


    