#Main program to run the Ball

import RPi.GPIO as GPIO
from LIS3DH import LIS3DH
from time import sleep

def main():
	
  sensor = LIS3DH()
	sensor.setRange(LIS3DH.RANGE_2G)
  
  while True:
    x = sensor.getX()
    y = sensor.getY()
    z = sensor.getZ()
    print("X = "+x)
    print("Y = "+y)
    print("Z = "+z)
    sleep(0.5)
