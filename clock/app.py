from clock import *
from time import sleep
from datetime import datetime

while True:
    sleep(1)
    d = datetime.now()
    # print(d.hour , d.minute ,d.second)
    printTime(d.hour , d.minute , d.second)
    DrowClock(d.hour , d.minute , d.second)

