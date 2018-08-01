import schedule
from time import gmtime, strftime
import time
import RPi.GPIO as GPIO

LED = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, GPIO.LOW)

def job():
	print("pintu ditutup")
	print strftime("%Y-%m-%d %H:%M:%S", gmtime())
	GPIO.output(LED, GPIO.HIGH)
#	time.sleep(2)
#	GPIO.output(LED, GPIO.LOW)
#	time.sleep(2)

def job2():
	print("pintu dibuka")
	print strftime("%Y-%m-%d %H:%M:%S", gmtime())
	GPIO.output(LED, GPIO.LOW)

schedule.every().day.at("22:14").do(job)
#schedule.every().day.at("22:15").do(job2)

while True:
	schedule.run_pending()
	time.sleep(1)
