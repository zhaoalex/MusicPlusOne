from music21 import *
from ScoreSystem import indexFromChord, calcCertainty

chordNameList = ["CM", "FM", "GM", "G7", "Am", "Dm", "Em", "Cm", "Fm", "Gm", "A-M", "Do", "E-M", "B-M"]

states = ["GM FM Am Dm Em".split(), "GM CM Dm".split(), "CM Cm Am FM A-M".split(), "CM Cm Am".split(), "FM Dm GM".split(), \
"GM".split(), "FM".split(), "GM Gm Fm A-M Do E-M B-M".split(), "GM Gm Cm Do".split(), "Cm A-M Fm".split(), "Fm Do".split(), \
"GM Gm".split(), "Fm A-M".split(), "E-M".split()] # options the chords can GO TO

# remember, we're assuming one chord per measure.
def stateMachine(melody1, harmony1, origCertainties, quality):
	allMeasures = melody1.getElementsByClass('Measure')
	allChords = harmony1.getElementsByClass('ChordSymbol')
	allChordsList = []
	for i in range(0, len(allChords)):
		allChordsList.append(allChords[i])
	for i in range(1, len(origCertainties)):
		if origCertainties[i] < 2.6:
			print(allChords[i])
			prevChord = allChords[i - 1]
			possIndex = indexFromChord(prevChord)
			print(possIndex)
			possibilities = states[possIndex]
			possibilities.insert(0, chordNameList[indexFromChord(prevChord)])
			newCertainties = []
			for j in range(0, len(possibilities)):
				tempChord = harmony.ChordSymbol(possibilities[j])
				newCertainties.append(calcCertainty(allMeasures[i], quality, tempChord))
				newCertainties[j] += 1.0
			possibilities.append(chordNameList[indexFromChord(allChords[i])])
			print(possibilities)
			newCertainties.append(origCertainties[i])
			print(newCertainties)
			mostCertainIndex = getMostCertain(newCertainties)
			print(mostCertainIndex)
			newChord = harmony.ChordSymbol(possibilities[mostCertainIndex])
			newChord.writeAsChord = True
			newChord.quarterLength = 4
			print(newChord)
			allChordsList[i] = newChord
	harmony2 = stream.Stream()
	for i in allChordsList:
		harmony2.append(i)
	return harmony2

def getMostCertain(certainties):
	index = 0
	maxCrtnty = certainties[0]
	for i in range(0, len(certainties)):
		if certainties[i] > maxCrtnty:
			index = i
			maxCrtnty = certainties[i]
	return index
