# import schedule
from time import sleep
from pyb import Pin, delay

def run_motorpump(number_of_steps):
	PUMP.low()
	for x in range(number_of_steps):
		PUMP.high()
		STEP.high()
		pyb.delay(5) #speed of step motor
		STEP.low()
		pyb.delay(5)
	PUMP.low()

DIR = Pin('X1',Pin.OUT_PP)
STEP = Pin('X2',Pin.OUT_PP)
PUMP = Pin('X3',Pin.OUT_PP)
DIR.high()

#using time scheduler 
# schedule.every(1440).minutes.do(run_motorpump(5000))
# while True:
# 	schedule.run_pending()
# 	sleep(1)

#using sleep
while True:
	run_motorpump(5000)
	sleep(86400) #run script daily