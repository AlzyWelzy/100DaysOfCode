with open("file.txt", "w") as f:
    print(type(f))

    f.write("Hello World!")

with open("file.txt", "r") as f:
    print(type(f))

    print(f.read())

    f.seek(4)

    print(f.read())
