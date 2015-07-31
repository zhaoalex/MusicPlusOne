# MusicPlusOne
A music harmonizer; given a melody, MusicPlusOne can generate the backing accompaniment!

MusicPlusOne **requires** the music21 library to function. Download music21 here: http://web.mit.edu/music21

MusicPlusOne was created for UCSD COSMOS 2015, Cluster 9: Music and Technology.

# How to use
NOTE: MusicPlusOne uses MIDI files for input and output. Your melody must be in the form of a MIDI file.

To open MusicPlusOne, open the file named: **start.py**

When MusicPlusOne is loaded, a GUI will pop up. click "Choose File" to choose your file, select the key your melody is in, and click "Harmonize" to harmonize or "Export to MIDI" to save the harmonization as a MIDI file.

If the score seems strange (32nd rests, for example), simply export to MIDI and open your MIDI file in MuseScore or equivalent.

# Current Limitations
* MusicPlusOne currently only functions in 4/4 time; any other time signature will not output correctly
* The smallest possible note duration is an 8th note
* Only adds tonal harmonics (no jazz harmonies, atonal harmonies, etc.)
* At times, the program may return a dissonant chord; this is because each chord always plays on the first beat while chords are calculated based on the entire measure
* Only monophonic melodies are harmonized; any chords in the melody will cause the program to choose an incorrect chord
* MusicPlusOne only generates one chord per measure
