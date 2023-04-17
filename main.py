from replit import audio
import time


# sine   - 1
# square - 2
# saw    - 3

piano_notes = {
    "A": 27.50,
    "A#": 29.14,
    "B": 30.87,
    "C": 32.70,
    "C#": 34.65,
    "D": 36.71,
    "D#": 38.89,
    "E": 41.20,
    "F": 43.65,
    "F#": 46.25,
    "G": 49.00,
    "G#": 51.91
}

def tone(dur, pitch, wave, oct):
  if type(pitch) == str:
    pitch = piano_notes[pitch]
  audio.play_tone(dur, pitch * oct, wave)
  time.sleep(dur)

tone(1, "C", 1, 10)