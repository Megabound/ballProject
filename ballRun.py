"""Main program to run the Ball"""
import sys
import time
#import Rpi.GPIO as GPIO

def checkCatch():
	"""Checks to see if the ball has been thrown and caught"""
	triggered = False
	accelerometer = 10
	setLevel = 5
	
	if accelerometer<setLevel:
		triggered = True
	
	return triggered

def playSound():
	"""Plays the next sound available on the USB drive"""
	return "Hell"

def switchLight():
	"""Switches the light to the next state"""
	return "Yeah"

def main():
	"""Main entry point for the program"""
	triggered = checkCatch()
	
	if triggered:
		print(playSound())
		time.sleep(1)
		print(switchLight())


if __name__ == '__main__':
	sys.exit(main())