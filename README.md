# MusicPlusOne
A music harmonizer; given a melody, MusicPlusOne can generate the backing accompaniment!

MusicPlusOne **requires** the music21 library to function. Download music21 here: http://web.mit.edu/music21

MusicPlusOne was created by Alex Zhao, Kalen Chang, Aditya Nadkarni, and Bryan Yang for the UCSD COSMOS 2015 Cluster 9 (Music and Technology) final project.

# How to use
NOTE: MusicPlusOne uses MIDI files for input and output. Your melody must be in the form of a MIDI file.

To open MusicPlusOne, open the file named: **start.py**

When MusicPlusOne is loaded, a GUI will pop up. click "Choose File" to choose your file, select the key your melody is in, and click "Export to MIDI" to harmonize your melody and save it as a MIDI file.

# Current Limitations
* MusicPlusOne currently only functions in 4/4 time; any other time signature will not output correctly
* The smallest possible note duration is an 8th note
* Only adds tonal harmonics (no jazz harmonies, atonal harmonies, etc.)
* At times, the program may return a chord that is dissonant from the melody; this is because all notes of the chord are played, and some of those notes may be dissonant with the melody
* Only monophonic melodies are harmonized; any chords in the melody will cause the program to choose an incorrect chord
* MusicPlusOne only generates one chord per measure

# Current Bugs
* Harmony may be an octave higher than it should be at times
* All data is currently stored in the first measure of melody instead of in the stream itself

# Debug
To run debug mode, simply run start.py from the terminal with the first argument as "debug": python start.py debug

In debug mode, an extra button will pop up saying "DEBUG: Hrmnize". By clicking that button, MusicPlusOne will harmonize directly instead of exporting to a MIDI file first. However, this will cause many visual, rhythm-based, and note-based errors, therefore making this option faster but much more broken. To fix all errors, simply export to MIDI instead and open in MuseScore or equivalent.

# Future goals
* Multiple chords per measure
* 16th note (or smaller) resolution
* Polyphonic melody support
* Generate harmony rhythm based on the melody
* Add more harmony rhythms
