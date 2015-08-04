from music21 import *
import Tkinter, tkFileDialog
from ScoreSystem import firstPass, calcCertainty
from StateMachine import stateMachine
from RhythmGen import genRhythm

score1 = None
keyOptions = ["C", "C#/Db", "D", "D#/Eb", "E", "F", "F#/Gb", "G", "G#/Ab", "A", "A#/Bb", "B"]

def separateMeasures(stream1): # only 4/4 for now; expand later?
	return stream1.makeMeasures()

def transposeStream(score1, keyName):
	n = keyOptions.index(keyName)
	try:
		score1.flat.transpose(-n, inPlace = True)
	except TypeError:
		pass
	return score1

def transposeBack(score1, keyName):
	n = keyOptions.index(keyName)
	try:
		score1.flat.transpose(n, inPlace = True)
	except TypeError:
		pass
	return score1

def harmonize(score1, quality): #TODO: REWRITE ALL CODE USING HARMONY.FIGURE
	harmony1 = stream.Stream()
	allCertainties = []
	for i in range(len(score1[0])): # first pass: SS
		# WHOLE RESTS DO NOT WORK
		chordName = firstPass(score1[0][i], quality)
		meChord = harmony.ChordSymbol(chordName)
		meChord.writeAsChord = True
		meChord.quarterLength = 4
		harmony1.append(meChord)
		allCertainties.append(calcCertainty(score1[0][i], quality, meChord))
	harmony2 = stateMachine(score1[0], harmony1, allCertainties, quality)
	harmony2 = genRhythm(harmony2)
	score1.insert(harmony2)
	return score1

def streamToMidi(filename):
	file2 = tkFileDialog.asksaveasfilename(title="Choose Save Location", initialfile=filename, defaultextension=".mid")
	m = midi.translate.streamToMidiFile(score1)
	m.open(file2, 'wb')
	m.write()
	m.close()

def doHarmonization(filename, key, quality): # put measure1 data in score
	global score1
	score1 = stream.Score()
	melody = converter.parse(filename)
	melody = separateMeasures(melody)
	melody = transposeStream(melody, key)
	score1.insert(melody)
	score1 = harmonize(score1, quality)
	score1 = transposeBack(score1, key)
	# score1.show('text')
	return score1
