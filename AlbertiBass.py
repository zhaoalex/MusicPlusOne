from music21 import *

def doAlbertiBass(harmony1):
    allChords = harmony1.getElementsByClass('Chord')
    harmony2 = stream.Stream()
    for i in range(0, len(allChords) - 1): # last measure will be just a chord
        pitchList = allChords[i].pitches
        if len(pitchList) == 3: # triad
            newMeasure = stream.Measure()
            for j in range(4):
                firstChord = chord.Chord()
                firstChord.pitches = pitchList[0:2]
                firstChord.quarterLength = 0.5
                secondChord = note.Note(pitchList[2])
                secondChord.quarterLength = 0.5
                newMeasure.append(firstChord)
                newMeasure.append(secondChord)
        elif len(pitchList) == 4: #7th
            newMeasure = stream.Measure()
            for j in range(2):
                for k in range(4):
                    nextNote = note.Note(pitchList[k])
                    nextNote.quarterLength = 0.5
                    newMeasure.append(nextNote)
        else: # just write the chord!
            newMeasure = stream.Measure()
            newMeasure.append(allChords[i])
        harmony2.append(newMeasure)
    newMeasure = stream.Measure()
    newMeasure.append(allChords[len(allChords) - 1])
    harmony2.append(newMeasure)
    return harmony2
