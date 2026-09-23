# Source - https://stackoverflow.com/a/40327294
# Posted by PythonProgrammi, modified by community. See post 'Timeline' for change history
# Retrieved 2026-09-24, License - CC BY-SA 4.0

'''
from win32com.client import Dispatch
speak = Dispatch("SAPI.SpVoice").Speak
speak("Ciao")
'''

from win32com.client import Dispatch

names = ["Vedant", "Ankit", "Amit", "Ravi", "Chaurasiya", "Ritik", "Nitin", "Shubham"]

speaker = Dispatch("SAPI.SpVoice")

for name in names:
    speaker.Speak(f"Shoutout to {name}")
