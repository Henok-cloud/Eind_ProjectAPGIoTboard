import apgiotboard
import time

# binair op en neer teller. werk door te drukken op s1 om  opwaarts te tellen en s2 om neerwaarts te tellen.
# teller bevat 6 oranje leds om van 0 tot 64 te kunnen tellen of aftellen.
# teller geeft aan aan door groene led als cijfer posetief is en rode led als deze negatief is.
BTN1 = 1
BTN2 = 2
LONG_MS = 1000
LED_OFFSET = 3 

def run():
    teller = 0
    prev1 = False
    prev2 = False
    t1 = 0
    t2 = 0
    t_both = None

    apgiotboard.all_leds_off()

    while True:

        now = time.ticks_ms()

        #--- check beide knoppen long-presses (exit)
        b1 =apgiotboard.button_pressed(BTN1)
        b2 = apgiotboard.button_pressed(BTN2)

        if b1 and b2:
            # zitten allebei ingedrukt
            if t_both is None:
                t_both = now
            elif time.ticks_diff(now, t_both) >= LONG_MS:
            # exit
                print(" Exit program ")
                apgiotboard.all_leds_off()
                return
        else:
            t_both = None

        # BTN1 kort press > teller ++
        if b1 and not prev1:
            #start press
            t1 = now
        elif not b1 and prev1:
            # release, check duration 
            if time.ticks_diff(now, t1) < LONG_MS:
                teller += 1
        prev1 = b1


        # ---- BTN2 kort press > teller -- --- 
        if b2 and not prev2:
            t2 = now
        elif not b2 and prev2:
            if time.ticks_diff(now,t2) < LONG_MS:
                teller -= 1
        prev2 = b2


        # --- Bereken en zet LEDs -- 
        # status LEDS:
        if teller >= 0:
            apgiotboard.led(2).on()
            apgiotboard.led(1).off()
        else:
            apgiotboard.led(1).on()
            apgiotboard.led(2).off()

        # binaire weergave: 
        bits = bin(abs(teller))[2:]
        #reset alle keer als je van bit-lengte wisselt?
        apgiotboard.all_leds_off()
        for i, bit in enumerate(reversed(bits)):
            if bit == "1":
                apgiotboard.led(i + LED_OFFSET).on()
        print(bits)      
      




