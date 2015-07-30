from music21 import *

chordList = [[0, 4, 7], [5, 9, 0], [7, 11, 2], [7, 11, 2, 5], [9, 0, 4], [2, 5, 9], [4, 7, 11], [0, 3, 7], \
[5, 8, 0], [7, 10, 2], [8, 0, 3], [2, 5, 8], [3, 7, 10], [10, 2, 5]]
chordNameList = ["CM", "FM", "GM", "G7", "Am", "Dm", "Em", "Cm", "Fm", "Gm", "A-M", "Do", "E-M", "B-M"]
majmin = [0, 0, 2, 2, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1] # 0 is Maj, 1 is min, 2 is both

def firstPass(measure1, quality):
	chordScore = calcScore(measure1, quality)
	chordName = findMaxIndex(chordScore)
	return chordName

#TODO: change certainty/chord for first and last measure
def calcCertainty(measure1, quality, chord):
	chordScore = calcScore(measure1, quality)
	revChordScore = calcRevScore(measure1, chordNameList[indexFromChord(chord)])
	return chordScore[indexFromChord(chord)] * revChordScore
	# remember that for all chord scores, 0.5 is added to each note in the chord! take into account later

#TODO: first and last measures: give tonic one extra pt
def calcScore(measure1, quality):
	chordScore = [0] * len(chordList)
	allNotes = measure1.getElementsByClass('Note')
	noteList = []
	for i in range(0, len(allNotes)):
		if allNotes[i].offset % 1.0 == 0.0:
			noteList.append(allNotes[i])
	for i in range(0, len(noteList)):
		noteList[i].quarterLength = roundNoteDurations(noteList[i])
	for i in range(0, len(noteList)):
		for j in range(0, len(chordList)):
			if noteList[i].pitchClass in chordList[j]:
				if i == 0:
					chordScore[j] += 1
				if quality == 0: # Major
					if majmin[j] == 1:
						chordScore[j] -= 0.5
				else: # minor
					if majmin[j] == 0:
						chordScore[j] -= 0.5
				chordScore[j] += noteList[i].quarterLength
	return chordScore

# @return string of chord; this only gives the first solution!
def findMaxIndex(chordScore):
	max = chordScore[0]
	maxIndex = 0
	for i in range(0, len(chordScore)):
		if chordScore[i] > max:
			max = chordScore[i]
			maxIndex = i

	return chordNameList[maxIndex]

# @return num notes in chord present / total notes in chord. maybe only consider the chordNameList relevant to that quality?
def calcRevScore(measure1, chordName):
	revChordScore = 0
	noteList = measure1.getElementsByClass('Note')
	index = chordNameList.index(chordName)
	usedChordPitches = [0] * len(chordList[index]) # 0 is unused, 1 is used
	for i in range(0, len(chordList[index])):
		for j in range(0, len(noteList)):
			if chordList[index][i] == noteList[j].pitchClass and usedChordPitches[i] == 0:
				revChordScore += 1
				usedChordPitches[i] = 1
	revChordScore /= float(len(chordList[index]))
	return revChordScore

def indexFromChord(chord):
	return chordList.index(chord.pitchClasses)

def roundNoteDurations(note): # this breaks 16th notes, but we're not using those!
	return int(note.quarterLength / 0.5 + 0.5) * 0.5
