from machine import Pin, PWM
import time


def run_motorpump(number_of_steps):
    PUMP.low()
    for x in range(number_of_steps):
        PUMP.high()
        STEP.high()
        time.sleep(0.005)
        STEP.low()
        time.sleep(0.005)
    PUMP.low()

DIR=Pin(23, Pin.OUT)
STEP=Pin(22, Pin.OUT)
PUMP=Pin(21, Pin.OUT)
DIR.on()

while True:
    run_motorpump(5000)
    time.sleep(86400) #run script daily
