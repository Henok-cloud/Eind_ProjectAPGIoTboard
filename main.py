# main.py (non-blocking button, live pot → LED update)
import time
import apgiotboard
from Op_neer_teller_binary import run as teller_run
from licht_balk_verdrijver_links_rechhts import run as balk_run
from LED_lichtshow import run as lightshow
from internal_temp import run as temppico

BTN1 = 1
BTN2 = 2
SHORT_MS = 200


funcs = {1: teller_run, 2: balk_run, 3: lightshow, 4:temppico}
N_FUNCS = len(funcs)

def map_dial_to_1_n():
    v = apgiotboard.dial_value()        # 0–65535
    sel = 1 + (v * N_FUNCS) // 65536
    return max(1, min(sel, N_FUNCS))

def show_selection(n):
    # zet LED n aan, de rest uit
    for i in range(1, N_FUNCS+1):
        apgiotboard.led(i).on() if i == n else apgiotboard.led(i).off()

def main():
    prev = False
    t0   = 0

    while True:
        sel = map_dial_to_1_n()
        show_selection(sel)

        cur = apgiotboard.button_pressed(BTN1)
        if cur and not prev:
            t0   = time.ticks_ms()
            prev = True
        elif not cur and prev:
            dur = time.ticks_diff(time.ticks_ms(), t0)
            if dur < SHORT_MS:
                funcs[sel]()          # roept teller_run() of balk_run()
            prev = False

        time.sleep_ms(20)

if __name__ == "__main__":
    main()

