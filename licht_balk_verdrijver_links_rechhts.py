import time
import apgiotboard



def licht_bak_verdrijver_links_rechts(snelhied_ms):

    while True:
        if apgiotboard.button_pressed(1,until_released=True):
            