import string
import random


def randChar():
    # create a string of 3 random characters
    return "".join(random.choice(string.ascii_letters) for _ in range(3))


def encode(str):
    if len(str) >= 3:
        str = randChar() + str[1:] + str[0] + randChar()
    return str[::-1]


def decode(str):
    if len(str) >= 3:
        str = str[4:-3] + str[3]
    return str[::-1]


encod = "Hello, I'm AlzyWelzy!"

print(encode(encod))

print(decode(encode(encod)))
