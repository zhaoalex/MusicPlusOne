from music21 import *
from ScoreSystem import indexFromChord, calcCertainty

chordNameList = ["CM", "FM", "GM", "G7", "Am", "Dm", "Em", "Cm", "Fm", "Gm", "A-M", "Do", "E-M", "B-M"]

states = ["GM FM Am Dm Em".split(), "GM CM Dm".split(), "CM Am FM A-M".split(), "CM Am".split(), "FM Dm GM".split(), \
"GM".split(), "FM".split(), "GM Gm Fm A-M Do E-M B-M".split(), "GM Gm Cm Do".split(), "Cm A-M Fm".split(), "Fm Do".split(), \
"GM Gm".split(), "Fm A-M".split(), "E-M".split()] # options the chords can GO TO

# one chord at a time
def stateMachine(melody1, harmony1, certainties, quality):
	melMeasures = melody1.getElementsByClass('Measure')
	allChords = harmony1.getElementsByClass('Chord')
	for i in range(0, len(allChords)):
		newCertainties = []
		if (certainties[i] < 2.6):
			if i != 0:
				chordOptions = states[indexFromChord(allChords[i - 1])]
				for j in chordOptions: # TODO: ASSUMING ONE CHORD PER MEASURE
					newMeasure = stream.Measure()
					newMeasure.append(allChords[i])
					newCertainties.append(calcCertainty(melMeasures[i], quality, allChords[i]) + 1)
				if chordNameList[indexFromChord(allChords[i])] not in chordOptions:
					chordOptions.append(chordNameList[indexFromChord(allChords[i])])
					newCertainties.append(certainties[i])
				index = -1
				maxCrnty = newCertainties[0]
				for j in range(0, len(newCertainties)):
					if newCertainties[j] > maxCrnty:
						index = j
				# print(chordOptions)
				print(newCertainties)
				newChord = harmony.ChordSymbol(chordOptions[index])
				newChord.writeAsChord = True
				newChord.quarterLength = 4
				allChords[i] = newChord
	return allChords
