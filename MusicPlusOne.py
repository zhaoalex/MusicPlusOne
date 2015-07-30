from music21 import *
import Tkinter, tkFileDialog
from ScoreSystem import firstPass, calcCertainty
from StateMachine import stateMachine

def midiToStream():
	file1 = tkFileDialog.askopenfilename(title="PUHLEEEZ Select a MIDI File kthxbai")
	score1 = converter.parse(file1)
	"""test = score1.getElementsByClass('Measure')
	for i in range(0, len(test)):
		print("LENGTH:" + test[i].quarterLengthFloat)"""
	return score1

def separateMeasures(stream1): # only 4/4 for now
	return stream1.makeMeasures()

def harmonize(score1):
	harmony1 = stream.Stream()
	allCertainties = []
	for i in range(0, len(score1[0])): # first pass
		chordName = firstPass(score1[0][i], 0)
		meChord = harmony.ChordSymbol(chordName)
		meChord.writeAsChord = True
		meChord.quarterLength = 4
		harmony1.append(meChord)
		allCertainties.append(calcCertainty(score1[0][i], 0, meChord))
		print(allCertainties)
		# harmony1 = harmony1.makeMeasures()
	allChords = stateMachine(harmony1, allCertainties, 0)
	harmony2 = stream.Stream()
	for i in allChords: # i can easily make this repeat: get the array of all certainties again, check if new certainties = old certainties
		harmony2.append(i)
	score1.insert(harmony1) # harmony2
	# score1.show('musicxml')
	# score1.show('text')
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
# score1.show('text')
score1.show('musicxml')

# streamToMidi(score1)
