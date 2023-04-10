# Work Only on Windows
# This is NOT Working on REPLIT (I don't know why!)
# But, Work on Other platforms .

import pyttsx3

engine = pyttsx3.init()
a = ["Harry", "Lalit", "Vishal", "Ganesh"]

for name in a:
    engine.say(f"Shoutout to {name}")

engine.runAndWait()
