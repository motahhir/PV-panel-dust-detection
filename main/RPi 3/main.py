import json
import requests
import RPi.GPIO as GPIO
from time import sleep
from Photo import Photo
import subprocess

DIR=10
STEP=8
PUMP=40
CLEAN_LED=12
DIRTY_LED=16
GPIO.setmode(GPIO.BOARD)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.setup(PUMP, GPIO.OUT)
GPIO.setup(CLEAN_LED, GPIO.OUT)
GPIO.setup(DIRTY_LED, GPIO.OUT)
GPIO.output(DIR, 1) #CLOCKWISE DIRECTION

keywords=['Clouds','Clear']

def check_weather():
	link="http://api.openweathermap.org/data/2.5/weather?q=Fes&appid=81856d49dfb92c91b514afcef157345f&units=metric"
	weather=requests.get(link)
	data=weather.json()
	main=data['weather']

	if any(keyword== main[0]['main'] for keyword in keywords) and main[0]['description']!='overcast clouds':
		return True
	else: 
		return False

def run_motorpump(number_of_steps):
	GPIO.output(PUMP, GPIO.LOW)
	for x in range(number_of_steps):
		GPIO.output(PUMP, GPIO.HIGH)
		GPIO.output(STEP,GPIO.HIGH)
		sleep(.005) #speed of step motor
		GPIO.output(STEP,GPIO.LOW)
		sleep(.005)
	GPIO.output(PUMP, GPIO.LOW)


if (check_weather()):
	subprocess.run('sudo raspistill -o /pi/home/inputimage.jpg', shell=True)
	sleep(10) #allow time for the camera to take and save the picture
	clean_pv=Photo(r'/pi/home/inputimage.jpg')
	clean_pv.segmentation() #binary thresholding
	clean_pv.computeGLCM() #computing GLCM matrix features
	if (clean_pv.checkfordust()): #returns True if contrast high
		GPIO.output(DIRTY_LED, GPIO.HIGH) #turns on RED Led
		run_motorpump(5000) #runs motor and pump simultaneously for 5000 steps
		GPIO.output(DIRTY_LED, GPIO.LOW)
	else:
		GPIO.output(CLEAN_LED, GPIO.HIGH) #turns on Green LED for 5 seconds
		sleep(5)
		GPIO.output(CLEAN_LED, GPIO.LOW)
	# clean_pv.append2df()
	# clean_pv.display()
	# print(clean_pv.df['Contrast'])
else:
	print("bad weather")

