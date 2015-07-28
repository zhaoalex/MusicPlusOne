from music21 import *

chordList = []
chords = []

def score(measure1, quality):
        global chordList
        global chords
	if quality == "Major":
		chordList = [[0, 4, 7], [5, 9, 0], [7, 11, 2], [7, 11, 2, 5], [9, 0, 4], [2, 5, 9], [4, 7, 11], [11, 2, 5]]
		chords = ["CM", "FM", "GM", "G7", "Am", "Dm", "Em", "Bo"]
	else:
		chordList = [[0, 3, 7], [5, 8, 0], [7, 10, 2], [7, 11, 2, 5], [8, 0, 3], [2, 5, 8], [3, 7, 10], [10, 2, 5], [11, 2, 5]]
		chords = ["Cm", "Fm", "Gm", "GM", "A-M", "Do", "E-M", "B-M", "Bo"]
	chordScore = assignScore(measure1)
	return findMaxIndex(chordScore)

def assignScore(measure1):
	chordScore = []
	for i in chordList:
		chordScore.append(0)
	noteList = measure1.getElementsByClass('Note')
	for i in range(0, len(noteList)):
		for j in range(0, len(chordList)):
			if noteList[i].pitchClass in chordList[j]:
				if i == 0:
					chordScore[j] += 1
				chordScore[j] += 1
	return chordScore

def findMaxIndex(chordScore): # @return string of chord; this only gives the first solution!
	max = chordScore[0]
	maxIndex = 0
	for i in range(0, len(chordScore)):
		if chordScore[i] > max:
			max = chordScore[i]
			maxIndex = i
			
	return chords[maxIndex]