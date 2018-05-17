"""Main program to run the Ball"""
import sys
import RPi.GPIO as GPIO
import SimpleMFRC522
from LIS3DH import LIS3DH
from time import sleep

def main():
	"""Main entry point for the program"""
	sensor = LIS3DH()
	sensor.setRange(LIS3DH.RANGE_2G)

	while True:
		x = abs(sensor.getX())
	        y = abs(sensor.getY())
	        z = abs(sensor.getZ())
	        average = (x+y+z)/3
	        print(average)
	        sleep(0.1)

if __name__ == '__main__':
	sys.exit(main())
