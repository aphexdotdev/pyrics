import time
import sys 

# ANSI escape code for ending colored lines
end = '\033[0m'

# Prints string one letter at a time
def printLine(str, speed = None, pause = None):
    
    if pause == None: pause = 20
    if speed == None: speed = 50 

    # Convert to ms
    speed = speed / 1000 
    pause = pause / 1000
    print(speed)
   
    # Printing
    for letter in str:
    
        if letter == '\n': time.sleep(0.5)
    
        print(f'{letter}', end="")
        time.sleep(speed)
        
        # Clear buffer
        sys.stdout.flush()
    else: 
        time.sleep(pause)
        print(' ')
