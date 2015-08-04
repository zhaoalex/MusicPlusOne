from music21 import *

def genRhythm(harmony1):
    allChords = harmony1.getElementsByClass('Chord')
    harmony2 = stream.Stream()
    for i in range(0, len(allChords) - 1): # last measure will be just a chord
        pitchList = allChords[i].pitches
        if len(pitchList) == 3: # triad
            newMeasure = albertiBass(pitchList)
        elif len(pitchList) == 4: #7th
            newMeasure = arpeggiated7th(pitchList)
        else: # just write the chord!
            newMeasure = stream.Measure()
            newMeasure.append(allChords[i])
        harmony2.append(newMeasure)
    newMeasure = stream.Measure()
    newMeasure.append(allChords[len(allChords) - 1])
    harmony2.append(newMeasure)
    return harmony2

def albertiBass(pitchList): #note1note5note3note5
    newMeasure = stream.Measure()
    for j in range(2):
        first = note.Note(pitchList[0])
        second = note.Note(pitchList[2])
        third = note.Note(pitchList[1])
        fourth = note.Note(pitchList[2])
        first.quarterLength = 0.5
        second.quarterLength = 0.5
        third.quarterLength = 0.5
        fourth.quarterLength = 0.5
        newMeasure.append(first)
        newMeasure.append(second)
        newMeasure.append(third)
        newMeasure.append(fourth)
    return newMeasure

def chord13note5(pitchList):
    newMeasure = stream.Measure()
    for j in range(4):
        firstChord = chord.Chord()
        firstChord.pitches = pitchList[0:2]
        firstChord.quarterLength = 0.5
        secondChord = note.Note(pitchList[2])
        secondChord.quarterLength = 0.5
        newMeasure.append(firstChord)
        newMeasure.append(secondChord)
    return newMeasure

def arpeggiated7th(pitchList):
    newMeasure = stream.Measure()
    for j in range(2):
        for k in range(4):
            nextNote = note.Note(pitchList[k])
            nextNote.quarterLength = 0.5
            newMeasure.append(nextNote)
    return newMeasure
