import time
import apgiotboard
import urandom


BTN1 = 1
BTN2 = 2
Long_ms = 2000
led_green = 1
led_red   = 2
led_start = 3
led_count = 6
rounds    = 5


def exit_pressed():
    start = time.ticks_ms()
    while apgiotboard.button_pressed(BTN1) and apgiotboard.button_pressed(BTN2):
        if time.ticks_diff(time.ticks_ms(), start)>= Long_ms:
            return True
        time.sleep_ms(10)
    return False

def run():
    socres = []
    apgiotboard.all_leds_off()

    for rnd in range(rounds):
        # 1) kies een willekeurige LED in 3-8
        idx = led_start + urandom.getrandbits(3)% led_count

        # 2) Toon en start timer
        apgiotboard.all_leds_off()
        apgiotboard.led(idx).on()
        t0 = time.ticks_ms()

        # 3) wacht op de juiste knop
        while True:
            if exit_pressed():
                apgiotboard.all_leds_off()
                return
            target_btn = BTN1 if idx < (led_start +led_count //2) else BTN2
            if apgiotboard.button_pressed(target_btn):
                dt = time.ticks_diff(time.ticks_ms(), t0)
                socres.append(dt)