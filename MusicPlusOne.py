from music21 import *
import Tkinter, tkFileDialog
from ScoreSystem import score

def midiToStream():
	file1 = tkFileDialog.askopenfilename(title="PUHLEEEZ Select a MIDI File kthxbai")
	stream1 = converter.parse(file1)

	return stream1

def separateMeasures(stream1): # only 4/4 for now
	return stream1.makeMeasures()

def harmonize(score1):
	harmony1 = stream.Stream()
	for i in range(0, len(score1[0])):
		chordName = score(score1[0][i], "Major")
		meChord = harmony.ChordSymbol(chordName)
		meChord.writeAsChord = True
		"""if chordName == "CM":
			meChord = chord.Chord([0, 4, 7])
		elif chordName == "FM":
			meChord = chord.Chord([5, 9, 0])
		elif chordName == "GM":
			meChord = chord.Chord([7, 11, 2])
		elif chordName == "G7":
			meChord = chord.Chord([7, 11, 2, 5])
		elif chordName == "Am":
			meChord = chord.Chord([9, 0, 4])
		elif chordName == "Dm":
			meChord = chord.Chord([2, 5, 9])
		elif chordName == "Em":
			meChord = chord.Chord([4, 7, 11])
		elif chordName == "Bo":
			meChord = chord.Chord([11, 2, 5])
		#minor
		elif chordName == "Cm":
			meChord = chord.Chord([0, 3, 7])
		elif chordName == "Fm":
			meChord = chord.Chord([5, 8, 0])
		elif chordName == "Gm":
			meChord = chord.Chord([7, 10, 2])
		elif chordName == "A-M":
			meChord = chord.Chord([8, 0, 3])
		elif chordName == "Do":
			meChord = chord.Chord([2, 5, 8])
		elif chordName == "E-M":
			meChord = chord.Chord([3, 7, 10])
		elif chordName == "B-M":
			meChord = chord.Chord([10, 2, 5])"""
		meChord.quarterLength = 4
		# meChord.transpose(interval.Interval(-12), inPlace=True)
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
