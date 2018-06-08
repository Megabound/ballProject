"""Main program to run the Ball"""
import sys
import glob
import pyglet
from time import sleep


def fileList(directory): #Returns a list of files in the specified directory
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
	"""Main entry point for the program"""
	catchRepeat=3
	tagRepeat=3
	catchCount=0
	playCount=0
	catchList, catchIndex = fileList("./catchSounds")
	print(catchList)
	print(catchIndex)
	pyglet.options["audio"] = ('openal', 'pulse', 'directsound','silent')

	while True:
		play = int(input("Press 1 for Play"))
		if play == 1:
			pyPlayer = pyglet.resource.media(catchList[catchIndex])
			pyPlayer.play()
			print("Sound!")
			sleep(3)
			catchCount+=1
			if catchCount == catchRepeat:
				catchCount=0
				catchIndex = updateIndex(catchList, catchIndex)
	sleep(0.1)

if __name__ == '__main__':
	sys.exit(main())
