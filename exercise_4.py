import string
import random
import os

N = 3


def lines(l="="):
    if l == "=":
        print("=" * 80)
    elif l == "-":
        print("-" * 80)
    else:
        print("Invalid line type")


def randChar():
    # create a string of 3 random characters
    return "".join(random.choice(string.ascii_letters) for _ in range(3))


def encode():
    str = input("Enter a string to encode: ")
    if len(str) >= N:
        str = randChar() + str[1:] + str[0] + randChar()
    return str[::-1]


def decode(str):
    if len(str) >= N:
        str = str[4:-3] + str[3]
    return str[::-1]


userInp = encode()

print("Encoded string: " + userInp)

decInp = decode(userInp)

print("Decoded string: " + decInp)
