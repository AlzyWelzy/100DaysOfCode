with open("file.txt", "w") as f:
    print(type(f))

    f.write("Hello World!")


with open("file.txt", "r") as f:
    print(type(f))

    print(f.tell())

    print(f.read())

    f.seek(4)

    print(f.tell())

    print(f.read())

with open("file.txt", "w") as f:
    f.write("Hello World!")

    f.truncate(5)


with open("file.txt", "r") as f:
    print(f.read())
