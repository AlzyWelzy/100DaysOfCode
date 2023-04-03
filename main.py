import os

if not os.path.exists("data"):
    # os.makedirs("data")
    os.mkdir("data")

for i in range(0, 100):
    with open(f"data/file_{i+1}.txt", "w") as f:
        f.write("Hello World!")

    # os.mkdir(f"data/day_{i+1}")
    with open(f"data/day_{i+1}/main.py", "w") as f:
        f.write("print('Hello World!')")
