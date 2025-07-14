import time
import apgiotboard


BTN1 = 1
BTN2 = 2
STOP_WIN = 300  #<0,5s Beide knoppen = stop-patroon
LONG_MS = 1000  # >1s beide knoppen = exit
LED_START = 3   # eerste oranje LED
LED_COUNT = 6   # aantal in de balk


def run():
    mode = None     # "left" , "richt", "stop" of none
    idx = LED_START
    direction = 1
    last_step =time.ticks_ms()
    stop_state =False

    prev1 = prev2 = False
    t1 = t2 = 0
    last_release = {BTN1: 0,BTN2:0}
    t_both = 0
    

    apgiotboard.all_leds_off()

    while True:
        now = time.ticks_ms()
        b1 = apgiotboard.button_pressed(BTN1)
        b2 = apgiotboard.button_pressed(BTN2)
        both = b1 and b2 

        # ---- long-press synch voor exit---
        if b1 and b2:
            # eerste gezamelijke druk
            if t_both ==0:
                t_both =now
            elif time.ticks_diff(now, t_both) >= LONG_MS:
                apgiotboard.all_leds_off()
                return
        else:
            t_both = 0
        
        # detecteren kort press op BTN1 en BTN2 --
        #BTN1
        if b1 and not prev1:
            t1 = now
        elif not b1 and prev1:
            dur1 = now - t1
            last_release[BTN1] = now
            if dur1 < LONG_MS:
                # kijk stop window
                lr2 = last_release[BTN2]
                if lr2 and abs(now - lr2) <= STOP_WIN:
                    mode = "stop"
                else:
                    mode = "left"
                    direction = 1
                    idx = LED_START
                    # clear before cumulative sweep
                    apgiotboard.all_leds_off()
                last_step = now
        prev1 = b1

        #BTN2
        if b2 and not prev2:
            t2 = now
        elif not b2 and prev2:
            dur2 = now - t2
            last_release[BTN2] = now
            if dur2 < LONG_MS:
                lr1 = last_release[BTN1]
                if lr1 and abs(now - lr1) <= STOP_WIN:
                    mode = "stop"
                else:
                    mode = "right"
                    direction = -1
                    idx = LED_START + LED_COUNT - 1
                    apgiotboard.all_leds_off()
                last_step = now
        prev2 = b2

        # -- LED-Update volgens mode
        delay = _get_delay()

        if mode in ("left", "right"):
            # cumulatieve
            if now - last_step >= delay:
                
                apgiotboard.led(idx).on()
                # next index met wrap-around
                idx += direction
                if idx < LED_START or idx >= LED_START + LED_COUNT:
                    apgiotboard.all_leds_off()
                    idx = LED_START if mode == "left" else LED_START + LED_COUNT -1
                last_step = now
        elif mode == "stop":
            #blink alle LEDs non_blocking
            if now - last_step >= delay:
                if stop_state:
                    apgiotboard.all_leds_off()
                else:
                    for i in range(LED_START, LED_START + LED_COUNT):
                        apgiotboard.led(i).on()
                stop_state =not stop_state
                last_step = now
        else:
            #geen mode gekozen alles uit idle
            apgiotboard.all_leds_off()

        time.sleep_ms(10)
def _get_delay():
    # map dial_value()(0-65535) naar een delay tussen 50 - 300ms. 
    v = apgiotboard.dial_value()
    print(v)
    # kleiner v > sneller sweep
    return int((300-50)*(65535-v)/65535+50)


