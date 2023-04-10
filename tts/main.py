import gtts
from playsound import playsound

# make request to google to get synthesis
tts = gtts.gTTS("za warudo toki wo tomare", lang="ja")

# save the audio file
tts.save("za_warudo.mp3")

# play the audio file
playsound("za_warudo.mp3")
