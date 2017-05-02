# encoding: utf-8
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

P_S = 20
CLK = 21
_DAT = 22

GPIO.setup(P_S, GPIO.OUT) # P/S
GPIO.setup(CLK, GPIO.OUT) # CLK
GPIO.setup(_DAT, GPIO.IN) # ~DAT

GPIO.cleanup()
