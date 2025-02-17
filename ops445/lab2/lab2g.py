#!/usr/bin/env python3
#Author: Darrien James
#Author ID: 140360199
#Date Create: 2025/02/16
import sys


timer = 3
if len(sys.argv) > 1:
    timer = int(sys.argv[1])



while timer != 0:
    print(timer)
    timer = timer - 1
print("blast off!")
