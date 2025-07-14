import apgiotboard
import time
from apgiotboard import both_long_pressed

# binair op en neer teller. werk door te drukken op s1 om  opwaarts te tellen en s2 om neerwaarts te tellen.
# teller bevat 6 oranje leds om van 0 tot 64 te kunnen tellen of aftellen.
# teller geeft aan aan door groene led als cijfer posetief is en rode led als deze negatief is.
BTN1 = 1
BTN2 = 2
LONG_MS = 1000

def run():
    teller = 0
    x=3
    apgiotboard.all_leds_off()
    while True:

        if both_long_pressed(BTN1, BTN2):
            return
        
       # zet groen led aan als cijfer posteftie is en rod led als deze negatief is. 
        binary =bin(teller)[2:]
        if teller >=0:
            apgiotboard.led(2).on()
            apgiotboard.led(1).off()
        else:
            apgiotboard.led(1).on()
            apgiotboard.led(2).off()

        # drukknop 1 word ingelezen.        
        if apgiotboard.button_pressed(1, until_released=True):
            # Teller wordt verhoogd met een.
            teller = teller+1
        # zet leds uit  die niet gebruikt worden als cijfer daalt in waardn.
            if len(binary) > len(bin(teller)[2:]):
                apgiotboard.all_leds_off()
        # zet leds aan of uit achtereenvolgend naargelang hun waarden 1= on , 0 = off. 
            for i , char in enumerate(reversed(bin(teller)[2:])):
        # geeft stand van teller weer op scherm voor controle, deze met leds die aan off uit staan.            
                print(f"led{i}:{char}")
                    
                if char=="1":
                            apgiotboard.led(i+x).on()
                            time.sleep_ms(50)
                            
                if  char=="0":
                            apgiotboard.led(i+x).off()
                            time.sleep_ms(50)
                
            print(bin(teller)[2:], teller)
            

        if apgiotboard.button_pressed(2,until_released=True):
            teller = teller-1
        # bij neerwaarts tellen worden leds uitgezet die niet meer gebruikt zijn.  
            if len(binary) > len(bin(teller)[2:]):
                apgiotboard.all_leds_off()
        
            for i , char in enumerate(reversed(bin(teller)[2:])):
                print(f"led{i}:{char}")
                if char=="1":
                    apgiotboard.led(i+x).on()
                    time.sleep_ms(50)
                    
                if  char=="0":
                    apgiotboard.led(i+x).off()
                    time.sleep_ms(50)
                   
                print(bin(teller)[2:],teller)

 
    