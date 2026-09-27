import subprocess
import time
import tkinter as tk
from tkinter import messagebox

REPEAT_INTERVAL = 5   # TEST: 10 seconds
# REPEAT_INTERVAL = 3600   # Use this for 1 hour


def speak():
    subprocess.run([
        "powershell",
        "-NoProfile",
        "-Command",
        "Add-Type -AssemblyName System.Speech; "
        "$voice = New-Object System.Speech.Synthesis.SpeechSynthesizer; "
        "$voice.Speak('Hey Vedant Behenkelund, Paani pile nhito mar jayega')"
    ])


def show_popup():
    root = tk.Tk()
    root.withdraw()

    messagebox.showinfo(
        "Water Reminder",
        "Hey Vedant Behenkelund, Paani pile nhito mar jayega!"
    )

    root.destroy()


while True:
    speak()
    show_popup()

    time.sleep(REPEAT_INTERVAL)