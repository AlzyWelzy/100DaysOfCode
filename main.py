import os

if not os.path.exists("data"):
    os.makedirs("data")

for i in range(0, 100):
    with open("data/file_%s.txt" % i, "w") as f:
        f.write("Hello World!")
