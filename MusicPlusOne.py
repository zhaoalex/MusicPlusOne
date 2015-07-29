from music21 import *
import Tkinter, tkFileDialog
from ScoreSystem import firstPass

def midiToStream():
	file1 = tkFileDialog.askopenfilename(title="PUHLEEEZ Select a MIDI File kthxbai")
	stream1 = converter.parse(file1)

	return stream1

def separateMeasures(stream1): # only 4/4 for now
	return stream1.makeMeasures()

def harmonize(score1):
	harmony1 = stream.Stream()
	for i in range(0, len(score1[0])):
		chordName = firstPass(score1[0][i], 0)
		meChord = harmony.ChordSymbol(chordName)
		meChord.writeAsChord = True
		meChord.quarterLength = 4
		harmony1.append(meChord)
	score1.insert(harmony1)
	score1.show('musicxml')
	return score1

def streamToMidi(score1):
	file2 = tkFileDialog.asksaveasfilename(title="PUHLEEEEEZ Choose Save Location kthxbai") + ".mid"
	m = midi.translate.streamToMidiFile(score1)
	m.open(file2, 'wb')
	m.write()
	m.close()

root = Tkinter.Tk()
root.withdraw()

score1 = stream.Score()
melody = midiToStream()
melody = separateMeasures(melody)
score1.insert(melody)
score1 = harmonize(score1)

# streamToMidi(score1)
