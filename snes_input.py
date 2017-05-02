# encoding: utf-8
import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

P_S = 20
CLK = 21
_DAT = 22

GPIO.setup(P_S, GPIO.OUT) # P/S
GPIO.setup(CLK, GPIO.OUT) # CLK

GPIO.setup(_DAT, GPIO.IN) # ~DAT


status = True

count = 0

sleeptime = 1.0/60/16/2

def tika(gpios, sleeptime):
    status = True
    for i in range(2):
        [GPIO.output(g, status) for g in gpios]
        time.sleep(sleeptime)
        status = not status

stack = []
prev_stack = []
print(" ".join(["B","Y","s","S","U","D","L","R","A","X","L","R","1","2","3","4"]))
while True:
    for i in range(16):
        if i == 0:
            stack = []
            tika([P_S, CLK], sleeptime)
        else:
            tika([CLK], sleeptime)
        # print "{:02d}".format(i), GPIO.input(_DAT)
        stack.append("P" if not GPIO.input(_DAT) else " ")
        if i == 15:
            if stack != prev_stack:
                print(" ".join(stack),end="\r")
            prev_stack = stack

GPIO.cleanup()
