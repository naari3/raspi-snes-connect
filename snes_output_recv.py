# encoding: utf-8
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

P_S = 20
CLK = 21
_DAT = 22

GPIO.setup(P_S, GPIO.IN)
GPIO.setup(CLK, GPIO.IN)
GPIO.setup(_DAT, GPIO.OUT)

clk_count = 0
p_s_count = 0

stats = (None, None)
prev_stats = (None, None)


while True:
    stats = GPIO.input(P_S), GPIO.input(CLK), GPIO.input(_DAT)
    if prev_stats != stats:
        # print('P/S:{} CLK:{} ~DAT:{}'.format(*stats))
        if stats[0] == 1:
            clk_count = 0
            p_s_count += 1
        if stats[1] == 1:
            clk_count += 1
            # print(clk_count)
        if clk_count == 1 or clk_count == 8:
            GPIO.output(_DAT, False)
        GPIO.output(_DAT, True)
        prev_stats = stats


GPIO.cleanup()
