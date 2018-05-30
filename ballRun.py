"""Main program to run the Ball"""
import sys
import RPi.GPIO as GPIO
import SimpleMFRC522
from LIS3DH import LIS3DH
from time import sleep

def readAccel(sensor):
	x = abs(sensor.getX())
	y = abs(sensor.getY())
	z = abs(sensor.getZ())
	average = (x+y+z)/3
	return average

def readRFID(reader):
	id = None
	text = None
	id, text = reader.read_no_block()
	return text

def main():
	"""Main entry point for the program"""
	sensor = LIS3DH()
	sensor.setRange(LIS3DH.RANGE_2G)
	reader = SimpleMFRC522.SimpleMFRC522()

	while True:
		average = readAccel(sensor)
		RFIDTag = readRFID(reader)
		if average>0.6:
			print("Caught!")
		if RFIDTag != None:
			print(RFIDTag)
	        sleep(0.1)

if __name__ == '__main__':
	sys.exit(main())
