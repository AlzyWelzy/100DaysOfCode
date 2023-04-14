import requests
import json
from gtts import gTTS
import os
from playsound import playsound


city = input("Enter the city name: ").title()

url = f"https://api.weatherapi.com/v1/current.json?key=e9a2346dfb1d4070abd160036231404&q={city.lower()}"


url = requests.get(url)

response = json.loads(url.text)


curr_str = ""

print(response["current"])
print(type(response["current"]))

for _ in response["current"].items():
    str = f"{_[0]} : {_[1]} "
    tts = gTTS(str, lang="en")
    tts.save(f"{_[0]}.mp3")
    curr_str += str
    if isinstance(_[1], dict):
        print(_[1])
        for __ in _[1].items():
            str = f"{__[0]} : {__[1]} "
            tts = gTTS(str, lang="en")
            tts.save(f"{__[0]}.mp3")
            curr_str += str

allDir = os.listdir()

for file in allDir:
    if file.endswith(".mp3"):
        # os.system(f"mpg321 {file}")
        playsound(file)
