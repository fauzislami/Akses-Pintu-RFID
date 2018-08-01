#!/usr/bin/env python
# -*- coding: utf8 -*-
 
import RPi.GPIO as GPIO
import MFRC522
import signal
import time
from time import gmtime, strftime
import datetime
import schedule
 
continue_reading = True
 
# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print ("Ctrl+C captured, ending read.")
    continue_reading = False
    GPIO.cleanup()
 
# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)
 
# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()
 
# Welcome message
print ("Welcome to the MFRC522 data read example")
print ("Press Ctrl-C to stop.")
 
# This loop keeps checking for chips. If one is near it will get the UID and authenticate
while continue_reading:
    
    # Scan for cards    
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
 
    # If a card is found
    if status == MIFAREReader.MI_OK:
        print ("Card detected")
    
    # Get the UID of the card
    (status,uid) = MIFAREReader.MFRC522_Anticoll()
 
    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:
 
        # Print UID
        print ("Card read UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3])+','+str(uid[4]))  
        # This is the default key for authentication
        key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
        
        # Select the scanned tag
        MIFAREReader.MFRC522_SelectTag(uid)
        
        #ENTER Your Card UID here
        my_uid = [151,58,120,137,92]
	now = datetime.datetime.now()
        #Configure LED Output Pin
	LED = 11
	LED2 = 29
	pintu = 13
	GPIO.setup(LED, GPIO.OUT)
	GPIO.output(LED, GPIO.LOW)
	GPIO.setup(LED2, GPIO.OUT)
	GPIO.setup(13, GPIO.IN)
#Check to see if card UID read matches your card UIDdef pintugerak():

	if uid == my_uid :
		print("Akses diterima")
		print now
		if now.hour <= 22 :
			print("silakan masuk")
			GPIO.output(LED, GPIO.LOW)
			time.sleep(10)
			b = GPIO.input(13)
			if b == 0 :
				GPIO.output(LED, GPIO.HIGH)
		else :
			print("sudah larut malam")
			GPIO.output(LED, GPIO.HIGH)

	else:
		print("Akses ditolak")
		GPIO.output(LED, GPIO.HIGH)
		GPIO.output(LED2, GPIO.HIGH)
		time.sleep(1)
		GPIO.output(LED2, GPIO.LOW)
		time.sleep(1)
		GPIO.output(LED2, GPIO.HIGH)
		time.sleep(1)
		GPIO.output(LED2, GPIO.LOW)

#	continue

#	else :                            #Don't open if UIDs don't match
#		print("Sudah larut malam !")
#		for i in range (5) :
#			GPIO.output(LED, GPIO.HIGH)
#			time.sleep(0.5)
#			GPIO.output(LED, GPIO.LOW)
#			time.sleep(0.5)

#	    p.ChangeDutyCycle(0)
##        # Authenticate
##        status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 8, key, uid)
##
##        # Check if authenticated
##        if status == MIFAREReader.MI_OK:
##            MIFAREReader.MFRC522_Read(8)
##            MIFAREReader.MFRC522_StopCrypto1()
##        else:
##            print "Authentication error"
