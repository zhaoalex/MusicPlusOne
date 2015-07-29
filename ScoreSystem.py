from music21 import *

chordList = [[0, 4, 7], [5, 9, 0], [7, 11, 2], [7, 11, 2, 5], [9, 0, 4], [2, 5, 9], [4, 7, 11], [0, 3, 7], \
[5, 8, 0], [7, 10, 2], [8, 0, 3], [2, 5, 8], [3, 7, 10], [10, 2, 5]]
chords = ["CM", "FM", "GM", "G7", "Am", "Dm", "Em", "Cm", "Fm", "Gm", "A-M", "Do", "E-M", "B-M"]
majmin = [0, 0, 2, 2, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1] # 0 is Maj, 1 is min, 2 is both

def firstPass(measure1, quality):
	chordScore = calcScore(measure1, quality)
	chordName = findMaxIndex(chordScore)
	return chordName

def calcScore(measure1, quality):
	chordScore = []
	for i in chordList:
		chordScore.append(0)
	allNotes = measure1.getElementsByClass('Note')
	noteList = []
	for i in range(0, len(allNotes)):
		if allNotes[i].offset % 1.0 == 0.0:
			noteList.append(allNotes[i])
	for i in range(0, len(noteList)):
		for j in range(0, len(chordList)):
			if noteList[i].pitchClass in chordList[j]:
				if i == 0:
					chordScore[j] += 1
				if quality == 0: # Major
					if majmin[j] == 0 or majmin[j] == 2:
						chordScore[j] += 0.5
				else: # minor
					if majmin[j] == 1 or majmin[j] == 2:
						chordScore[j] += 0.5
				chordScore[j] += 1.0
	return chordScore

def findMaxIndex(chordScore): # @return string of chord; this only gives the first solution!
	max = chordScore[0]
	maxIndex = 0
	for i in range(0, len(chordScore)):
		if chordScore[i] > max:
			max = chordScore[i]
			maxIndex = i

	return chords[maxIndex]
