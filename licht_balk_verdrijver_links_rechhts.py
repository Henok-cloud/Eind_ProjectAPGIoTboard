# func1.py
import time
import apgiotboard
from apgiotboard import both_long_pressed


BTN1 = 1
BTN2 = 2
LONG_MS = 1000


def run():


    idx = 1
    direction = 1
    while True:
        # zet alle LEDs uit, zet één LED aan
        for i in range(1, 6):
            apgiotboard.led(i).off()
        apgiotboard.led(idx).on()

        # schuif idx
        idx += direction
        if idx == 5 or idx == 1:
            direction *= -1

        time.sleep_ms(200)

        # exit-voorwaarde
        if both_long_pressed(BTN1, BTN2, 1000 ):
            # zorg dat LEDs uit zijn
            for i in range(1, 6):
                apgiotboard.led(i).off()
            break