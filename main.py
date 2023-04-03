import os

if not os.path.exists("data"):
    os.makedirs("data")

for i in range(0, 100):
    with open(f"data/file_{i+1}.txt", "w") as f:
        f.write("Hello World!")
