import gtts
from playsound import playsound
import os

# make request to google to get synthesis
# tts = gtts.gTTS("za warudo toki wo tomare", lang="ja")
# tts = gtts.gTTS("za warudo toki wo tomare", lang="ja", slow=False)
tts = gtts.gTTS(
    "ehe te nan desu ka",
    lang="ja",
)

# save the audio file
tts.save("za_warudo.mp3")

# play the audio file
playsound("za_warudo.mp3")


names = [
    "Manvendra Rajpoot",
    "Tarun Ghawri",
    "Madhur Chaturvedi",
    "Farhan Qazi",
    "Arfat Khan",
    "Vishal Sahu",
    "Yash Namdev",
]

tts = gtts.gTTS("Shoutout to " + ", ".join(names), lang="en")

tts.save("shoutout.mp3")

# playsound("shoutout.mp3")


for name in names:
    tts = gtts.gTTS(f"Shoutout to {name}", lang="en")
    tts.save(f"shoutout_{name}.mp3")

    # playsound(f"shoutout_{name}.mp3")

all = os.listdir()

for file in all:
    if file.endswith(".mp3"):
        playsound(file)
