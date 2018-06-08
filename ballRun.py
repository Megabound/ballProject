#Main program to run the Ball

import sys
import RPi.GPIO as GPIO
import SimpleMFRC522
import pyglet
import glob
from LIS3DH import LIS3DH
from time import sleep

def readAccel(sensor): #Reads the data from the accelerometer
	x = abs(sensor.getX())
	y = abs(sensor.getY())
	z = abs(sensor.getZ())
	average = (x+y+z)/3 #Averages all the readings
	return average

def readRFID(reader): #Reads the data from the RFID tag and returns the text stored
	id = None
	text = None
	id, text = reader.read_no_block()
	return text

def fileList(directory): #Returns a list of files in the specified directory, in the correct format for Pyglet
	list = glob.glob("./" + directory + "/*")
	for i in range(0,len(list)):
		list[i]=list[i][4:]
	return list, 0

def updateIndex(list, index): #Updates the playlist index
	index += 1
	if index >= len(list):
		index = 0
	return index

def main():
	
	#User Configuration#
	throwThreshold = 0.7 #Sensitivity for catch detaction, larger number = less sensitive
	catchRepeat=3 #Number of times the ball should repeat a word in catch mode
	tagRepeat=0 #Number of times the ball should repeat a word in RFID mode
	#End user configuration

	pyglet.options["audio"] = ('openal', 'pulse', 'directsound','silent')
	catchCount=0
	tagCount=0
	sensor = LIS3DH()
	sensor.setRange(LIS3DH.RANGE_2G)
	reader = SimpleMFRC522.SimpleMFRC522()

	rfidList, rfidIndex = fileList("./rfidSounds")
	catchList, catchIndex = fileList("./catchSounds")

	while True:
		average = readAccel(sensor)
		RFIDTag = readRFID(reader)
		if average>throwThreshold:
			pyPlayer = pyglet.resource.media(catchList[catchIndex])
			pyPlayer.play()
			print("Caught!")
			sleep(3)
			catchCount+=1
			if catchCount == catchRepeat:
				catchCount=0
				catchIndex = updateIndex(catchList, catchIndex)
		if RFIDTag != None:
			pyPlayer = pyglet.resource.media(rfidList[rfidIndex])
			pyPlayer.play()
			print(RFIDTag)
			tagCount+=1
			if tagCount == tagRepeat:
				tagCount=0
				rfidIndex = updateIndex(rfidList,rfidIndex)
		sleep(0.1)

if __name__ == '__main__':
	sys.exit(main())
