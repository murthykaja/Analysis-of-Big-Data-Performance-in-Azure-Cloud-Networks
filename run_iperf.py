import os
import sys
import time
import datetime

now_now = datetime.datetime.now()
tomorrow=datetime.datetime(2021,11,16,21,0)
print(now_now)
print(tomorrow)
while(now_now<tomorrow):
    os.system("iperf3 -c 20.121.14.59 -p 8080 -bidir -i 1 -t 5 >>out.txt")
    time.sleep(30)
    now_now = datetime.datetime.now()

