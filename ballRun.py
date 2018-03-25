"""Main program to run the Ball"""
import sys
import time

def checkCatch():
	triggered = False
	accelerometer = 10
	setLevel = 5
	"""Checks to see if the ball has been thrown and caught"""
	if accelerometer>setLevel:
		return True
	else:
		return False

def switchLight():
	"""Switches the light to the next state"""
	return "Hell"

def playSound():
	"""Plays the next sound available on the USB drive"""
	return "Yeah"

def main():
	"""Main entry point for the program"""
	triggered = checkCatch
	if triggered:
		print(playSound())
		time.sleep(5)
		print(switchLight())


if __name__ == '__main__':
	sys.exit(main())