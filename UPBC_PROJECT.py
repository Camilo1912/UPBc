"""
Useless pgrogress bar (UPBC-PROJECT)
VERSION 1.0
AUTOR: Camilo Marilaf Miranda
RELEASE DATE: 27-JUN-2020
DESCRIPTION: Useless-progress-bar (UPBC) it's useless, it's not like the others common progress bars, it's a powerful tool for your program if you want to have plenty of time to do whatever you want while also annoying whoever is using it, use it wisely.
""" 
import os
import random
import time

os.system("cls")

annoyingness_lvl = 2 #Change this number to select the level of annoyingness you want to apply, remember, higher the number, higher the pain.

i = 1
while i <= 100:
    time.sleep(random.uniform(0.02, annoyingness_lvl))
    os.system("cls")
    porciento = f"{i}%"
    print(f"\n\n\t{format('Wow!... Much Calculations.', '^52')}\n\t[{format('='*(int(i/2)), '<50')}]\n\t{porciento:^52}\n")
    if i < 20:
        print(f"\t{format('Hello there! I am Progressbar-chan OwO', '^52')}")
    elif i >= 20 and i < 33:
        print(f"\t{format('This acctually just take a WHILE...', '^52')}")
    elif i >= 33 and i < 66:
        print(f"\t{format('Meanwhile, you could do some random things!','^52')}\n\t{format('I also do random things...','^52')}")
    elif i >= 66 and i < 99:
        print(f"\t{format('Like count to one hundred!','^52')}\n\t{format('In random intervals of time...','^52')}")
    elif i == 99:
        print(f"\t{format('Just one more minute!', '^52')}")
        time.sleep(30)
        print(f"\t{format('...Literally', '^52')}")
        time.sleep(30)
    elif i == 100:
        time.sleep(0.5)
    i += 1
