import time

timestamp = time.strftime("%H:%M:%S")
print(timestamp)

if timestamp < "12:00:00":
    print("Good morning!")
elif timestamp < "17:00:00":
    print("Good afternoon!")
elif timestamp < "21:00:00":
    print("Good evening!")
else:
    print("Good night!")
