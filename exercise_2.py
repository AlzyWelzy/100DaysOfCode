import time

t = time.strftime("%H:%M:%S")
hour = int(t.strftime("%H"))

print(hour)

if hour >= 0 and hour < 12:
    print("Good morning!")
elif hour >= 12 and hour < 18:
    print("Good afternoon!")
elif hour >= 18 and hour < 24:
    print("Good evening!")
else:
    print("Invalid time!")

print("The current time is " + t)
