import sys
import time
from os import system , name

#animation=[ "10%" , "20%" , "30%" , "40%" , "50%" , "60%" , "70%" , "80%" , "90%" , "100%" ]
animation= ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
for i in range(len(animation)):
    time.sleep(0.1)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()
#to clear screen
# clear = lambda: os.system('cls')
def clear():
    if name=='nt':
        _=system('cls')
    else:
        _=system('clear')
time.sleep(1)
clear()
print("Done!")
print('\n')
