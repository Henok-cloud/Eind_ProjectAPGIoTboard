import apgiotboard
import time



def op_neer_teller ():
    teller = 0
    x=3
    apgiotboard.all_leds_off()
    while True:
        
       # time.sleep_ms(100)
        binary =bin(teller)[2:]
        if teller >=0:
            apgiotboard.led(2).on()
            apgiotboard.led(1).off()
        else:
            apgiotboard.led(1).on()
            apgiotboard.led(2).off()

               
        if apgiotboard.button_pressed(1, until_released=True):
            # Teller wordt verhoogd met een.
            teller = teller+1

            if len(binary) > len(bin(teller)[2:]):
                apgiotboard.all_leds_off()
        
            for i , char in enumerate(reversed(bin(teller)[2:])):
               #print(f"The number is now {teller} in binary {binary}")
                print(f"led{i}:{char}")
                #zet leds aan of uit aan de hand van led id= i en char= 1 of 0.
                if char=="1":
                    apgiotboard.led(i+x).on()
                    time.sleep_ms(50)
                    
                if  char=="0":
                    apgiotboard.led(i+x).off()
                    time.sleep_ms(50)
            
                print(bin(teller)[2:], teller)
            

        if apgiotboard.button_pressed(2,until_released=True):
            teller = teller-1
          
            if len(binary) > len(bin(teller)[2:]):
                apgiotboard.all_leds_off()
        
            for i , char in enumerate(reversed(bin(teller)[2:])):
               #print(f"The number is now {teller} d in binary {binary}")
                print(f"led{i}:{char}")
                if char=="1":
                    apgiotboard.led(i+x).on()
                    time.sleep_ms(50)
                    
                if  char=="0":
                    apgiotboard.led(i+x).off()
                    time.sleep_ms(50)
                   
                print(bin(teller)[2:],teller)
                
            
        
      
        


    
op_neer_teller()