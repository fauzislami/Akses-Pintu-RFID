import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.IN)
GPIO.setup(11, GPIO.OUT)
GPIO.output(11, 0)

while True:
	i = GPIO.input(13)
	if i == 0 :
		GPIO.output(11, 1)
