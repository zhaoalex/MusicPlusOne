from music21 import *
import Tkinter, tkFileDialog
from ScoreSystem import firstPass, calcCertainty
from StateMachine import stateMachine

score1 = None
keyOptions = ["C", "C#/Db", "D", "D#/Eb", "E", "F", "F#/Gb", "G", "G#/Ab", "A", "A#/Bb", "B"]

def midiToStream(filename):
	score1 = converter.parse(filename)
	return score1

def separateMeasures(stream1): # only 4/4 for now
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

def harmonize(score1, quality):
	harmony1 = stream.Stream()
	allCertainties = []
	for i in range(0, len(score1[0])): # first pass: SS
		# WHOLE RESTS DO NOT WORK
		chordName = firstPass(score1[0][i], quality)
		meChord = harmony.ChordSymbol(chordName)
		meChord.writeAsChord = True
		meChord.quarterLength = 4
		harmony1.append(meChord)
		allCertainties.append(calcCertainty(score1[0][i], quality, meChord))
	allChordsPass1 = stateMachine(score1[0], harmony1, allCertainties, quality)
	harmony2 = stream.Stream()
	for i in allChordsPass1:
		harmony2.append(i)
	if (harmony2.getElementsByClass('ChordSymbol')[0].bass().octave > 3):
		try:
			harmony2.flat.transpose(-12, inPlace = True)
		except TypeError:
			pass
	score1.insert(harmony2)
	return score1
def streamToMidi():
	file2 = tkFileDialog.asksaveasfilename(title="Choose Save Location") + ".mid"
	m = midi.translate.streamToMidiFile(score1)
	m.open(file2, 'wb')
	m.write()
	m.close()

def doHarmonization(filename, key, quality):
	global score1
	score1 = stream.Score()
	melody = midiToStream(filename)
	melody = separateMeasures(melody)
	melody = transposeStream(melody, key)
	score1.insert(melody)
	score1 = harmonize(score1, quality)
	score1 = transposeBack(score1, key)
	return score1
