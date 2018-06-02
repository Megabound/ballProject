"""Main program to run the Ball"""
import sys
import RPi.GPIO as GPIO
import SimpleMFRC522
import vlc
import glob
from LIS3DH import LIS3DH
from time import sleep

def readAccel(sensor): #Reads the data from the accelerometre
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

def fileList(directory): #Returns a list of files in the specified directory
	list = glob.glob("./" + directory + "/*")
	return list, 0

def updateIndex(list, index): #Updates the playlist index
	index += 1
	if index >= len(list):
		index = 0
	return index

def main():
	"""Main entry point for the program"""
	sensor = LIS3DH()
	sensor.setRange(LIS3DH.RANGE_2G)
	reader = SimpleMFRC522.SimpleMFRC522()

	rfidList, rfidIndex = fileList("./rfidSounds")
	catchList, catchIndex = fileList("./catchSounds")
	print(catchList)
	print(catchIndex)

	while True:
		average = readAccel(sensor)
		RFIDTag = readRFID(reader)
		if average>0.6:
			player = vlc.MediaPlayer(catchList[catchIndex])
			player.play()
			print("Caught!")
			catchIndex = updateIndex(catchList, catchIndex)
		if RFIDTag != None:
			player = vlc.MediaPlayer(rfidList[rfidIndex])
			player.play()
			print(RFIDTag)
			rfidIndex = updateIndex(rfidList,rfidIndex)
	        sleep(0.1)

if __name__ == '__main__':
	sys.exit(main())
